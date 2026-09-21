from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import grpc

import demand_forecast_pb2
import demand_forecast_pb2_grpc
import inventory_pb2
import inventory_pb2_grpc
from fastapi.middleware.cors import CORSMiddleware


# Arquivo: api-rest/main.py
# Descrição: Implementa a API REST (FastAPI) que orquestra os microserviços gRPC.
# Responsabilidade principal:
# - Recebe requisições HTTP do frontend
# - Chama o serviço de previsão de demanda (gRPC)
# - Chama o serviço de otimização de inventário (gRPC)
# - Combina as respostas e retorna uma recomendação consolidada
app = FastAPI(
    title="ISCF Lab 3 - Inventory Recommendation API",
    description="REST API that orchestrates the Demand Forecasting and Inventory Optimization gRPC microservices.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecommendationRequest(BaseModel):
    item_id: str
    warehouse_id: str
    historical_demand: List[int]
    forecast_horizon: int
    current_stock: int
    reorder_level: int
    safety_stock: Optional[int] = 0
    supplier_lead_time: Optional[int] = 0


class RecommendationResponse(BaseModel):
    item_id: str
    warehouse_id: str
    predicted_demand: int
    forecast_confidence: float
    forecast_horizon: int
    current_stock: int
    reorder_level: int
    safety_stock: int
    supplier_lead_time: int
    reorder_quantity: int
    inventory_adjustment_action: str
    explanation_message: str


@app.get("/")
def root():
    return {
        "message": "ISCF Lab 3 REST API is running.",
        "available_endpoint": "/recommendation"
    }


@app.post("/recommendation", response_model=RecommendationResponse)
def create_recommendation(request: RecommendationRequest):
    try:
        # -------------------------------------------------------
        # 1. Chamada ao MS1 - Serviço de Previsão de Demanda (gRPC)
        #    - Cria canal gRPC para o serviço de forecast
        #    - Monta a requisição com os dados históricos fornecidos
        #    - Recebe a previsão (predicted_demand, confidence, horizon)
        # -------------------------------------------------------
        forecast_channel = grpc.insecure_channel("localhost:50052")
        forecast_stub = demand_forecast_pb2_grpc.DemandForecastStub(forecast_channel)

        forecast_request = demand_forecast_pb2.DemandForecastRequest(
            item_id=request.item_id,
            historical_demand=request.historical_demand,
            forecast_horizon=request.forecast_horizon,
            warehouse_id=request.warehouse_id
        )

        forecast_response = forecast_stub.PredictDemand(forecast_request)

        # -------------------------------------------------------
        # 2. Chamada ao MS2 - Serviço de Otimização de Inventário (gRPC)
        #    - Cria canal gRPC para o serviço de inventário
        #    - Envia os dados relevantes (estoque atual + demanda prevista)
        #    - Recebe a recomendação de reorder/ação de inventário
        # -------------------------------------------------------
        inventory_channel = grpc.insecure_channel("localhost:50051")
        inventory_stub = inventory_pb2_grpc.InventoryOptimizationStub(inventory_channel)

        inventory_request = inventory_pb2.InventoryRequest(
            item_id=request.item_id,
            current_stock=request.current_stock,
            predicted_demand=forecast_response.predicted_demand,
            reorder_level=request.reorder_level,
            safety_stock=request.safety_stock,
            supplier_lead_time=request.supplier_lead_time
        )

        inventory_response = inventory_stub.OptimizeInventory(inventory_request)

        action_name = inventory_pb2.InventoryAdjustmentAction.Name(
            inventory_response.inventory_adjustment_action
        )

        # -------------------------------------------------------
        # 3. Monta e retorna a resposta REST combinando forecast + inventory
        #    - Converte o enum de ação para string
        #    - Empacota todos os campos no modelo `RecommendationResponse`
        # -------------------------------------------------------
        return RecommendationResponse(
            item_id=request.item_id,
            warehouse_id=request.warehouse_id,
            predicted_demand=forecast_response.predicted_demand,
            forecast_confidence=forecast_response.forecast_confidence,
            forecast_horizon=forecast_response.forecast_horizon,
            current_stock=request.current_stock,
            reorder_level=request.reorder_level,
            safety_stock=request.safety_stock,
            supplier_lead_time=request.supplier_lead_time,
            reorder_quantity=inventory_response.reorder_quantity,
            inventory_adjustment_action=action_name,
            explanation_message=inventory_response.explanation_message
        )

    except grpc.RpcError as e:
        raise HTTPException(
            status_code=400,
            detail={
                "grpc_status": str(e.code()),
                "grpc_details": e.details()
            }
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
