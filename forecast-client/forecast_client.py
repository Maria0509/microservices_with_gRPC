import grpc

import demand_forecast_pb2
import demand_forecast_pb2_grpc


# Arquivo: forecast-client/forecast_client.py
# Descrição: Cliente de teste para o serviço de previsão de demanda.
# Finalidade:
# - Montar cenários de input (histórico de vendas, horizonte de previsão)
# - Invocar o método `PredictDemand` e apresentar os resultados
def print_response(response):
    # Exibe os campos retornados pelo serviço de forecast
    print("Response from Demand Forecast Service:")
    print(f"Item ID: {response.item_id}")
    print(f"Predicted Demand: {response.predicted_demand}")
    print(f"Forecast Confidence: {response.forecast_confidence}")
    print(f"Forecast Horizon: {response.forecast_horizon}")


def run():
    # Conecta ao serviço de forecast que roda na porta 50052
    channel = grpc.insecure_channel("localhost:50052")
    stub = demand_forecast_pb2_grpc.DemandForecastStub(channel)

    # Cenários de teste para validar respostas e tratamento de erros
    test_scenarios = [
        {
            "name": "Scenario 1 - Normal demand forecast",
            "request": demand_forecast_pb2.DemandForecastRequest(
                item_id="ITEM001",
                historical_demand=[40, 45, 50, 55],
                forecast_horizon=1,
                warehouse_id="WH001"
            )
        },
        {
            "name": "Scenario 2 - Forecast for longer horizon",
            "request": demand_forecast_pb2.DemandForecastRequest(
                item_id="ITEM002",
                historical_demand=[20, 25, 30, 35, 40],
                forecast_horizon=2,
                warehouse_id="WH001"
            )
        },
        {
            "name": "Scenario 3 - Low number of historical values",
            "request": demand_forecast_pb2.DemandForecastRequest(
                item_id="ITEM003",
                historical_demand=[10, 15],
                forecast_horizon=1,
                warehouse_id="WH002"
            )
        },
        {
            "name": "Scenario 4 - Invalid empty Item ID",
            "request": demand_forecast_pb2.DemandForecastRequest(
                item_id="",
                historical_demand=[40, 45, 50],
                forecast_horizon=1,
                warehouse_id="WH001"
            )
        },
        {
            "name": "Scenario 5 - Invalid empty historical demand",
            "request": demand_forecast_pb2.DemandForecastRequest(
                item_id="ITEM005",
                historical_demand=[],
                forecast_horizon=1,
                warehouse_id="WH001"
            )
        },
        {
            "name": "Scenario 6 - Invalid negative demand value",
            "request": demand_forecast_pb2.DemandForecastRequest(
                item_id="ITEM006",
                historical_demand=[40, -10, 50],
                forecast_horizon=1,
                warehouse_id="WH001"
            )
        },
        {
            "name": "Scenario 7 - Invalid forecast horizon",
            "request": demand_forecast_pb2.DemandForecastRequest(
                item_id="ITEM007",
                historical_demand=[40, 45, 50],
                forecast_horizon=0,
                warehouse_id="WH001"
            )
        }
    ]

    for scenario in test_scenarios:
        print("\n" + "=" * 70)
        print(scenario["name"])
        print("=" * 70)

        try:
            # Efetua a chamada RPC e imprime o resultado
            response = stub.PredictDemand(scenario["request"])
            print_response(response)

        except grpc.RpcError as e:
            # Exibe status e detalhes em caso de erro gRPC
            print("gRPC error received from server:")
            print(f"Status code: {e.code()}")
            print(f"Details: {e.details()}")


if __name__ == "__main__":
    run()