from concurrent import futures
import grpc

import inventory_pb2
import inventory_pb2_grpc


# Arquivo: inventory/server.py
# Descrição: Implementa o servidor gRPC para otimização de inventário.
# Responsabilidades principais:
# - Validar os dados recebidos em cada request
# - Calcular a quantidade alvo de estoque e a ação recomendada
# - Suportar requisições unitárias (`OptimizeInventory`) e streaming (`OptimizeInventoryStream`)
class InventoryOptimizationService(
    inventory_pb2_grpc.InventoryOptimizationServicer
):
    # Método auxiliar interno: valida a requisição e calcula a resposta de inventário
    # Entrada: `request` contém os campos definidos em inventory.proto
    # Saída: `inventory_pb2.InventoryResponse` ou None (em caso de erro, contexto gRPC é atualizado)
    def calculate_inventory_response(self, request, context):
        item_id = request.item_id
        current_stock = request.current_stock
        predicted_demand = request.predicted_demand
        reorder_level = request.reorder_level
        safety_stock = request.safety_stock
        supplier_lead_time = request.supplier_lead_time

        if not item_id:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Item ID cannot be empty.")
            return None

        if current_stock < 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Current stock must be non-negative.")
            return None

        if predicted_demand < 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Predicted demand must be non-negative.")
            return None

        if reorder_level < 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Reorder level must be non-negative.")
            return None

        if safety_stock < 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Safety stock must be non-negative.")
            return None

        if supplier_lead_time < 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Supplier lead time must be non-negative.")
            return None

        target_stock = predicted_demand + reorder_level + safety_stock

        if supplier_lead_time > 0:
            lead_time_buffer = int(predicted_demand * 0.1 * supplier_lead_time)
        else:
            lead_time_buffer = 0

        target_stock += lead_time_buffer

        if current_stock < target_stock:
            reorder_quantity = target_stock - current_stock
            action = inventory_pb2.REORDER
            explanation_message = (
                f"Current stock ({current_stock}) is below the required target stock "
                f"({target_stock}). A reorder of {reorder_quantity} units is recommended."
            )

        elif current_stock > target_stock * 1.5:
            reorder_quantity = 0
            action = inventory_pb2.SCALE_DOWN
            explanation_message = (
                f"Current stock ({current_stock}) is significantly above the required "
                f"target stock ({target_stock}). Inventory level can be scaled down."
            )

        else:
            reorder_quantity = 0
            action = inventory_pb2.NO_ACTION
            explanation_message = (
                f"Current stock ({current_stock}) is sufficient for the predicted demand. "
                "No inventory adjustment is required."
            )

        return inventory_pb2.InventoryResponse(
            item_id=item_id,
            reorder_quantity=reorder_quantity,
            inventory_adjustment_action=action,
            explanation_message=explanation_message
        )

    # Método gRPC: processamento de uma única requisição de otimização
    # Recebe: `InventoryRequest` e retorna `InventoryResponse`
    def OptimizeInventory(self, request, context):
        response = self.calculate_inventory_response(request, context)

        # Se a validação falhar, `calculate_inventory_response` retorna None
        if response is None:
            return inventory_pb2.InventoryResponse()

        return response

    # Método gRPC: processamento via server-streaming para múltiplos itens
    # Recebe um `InventoryBatchRequest` e gera múltiplas `InventoryResponse`
    def OptimizeInventoryStream(self, request, context):
        print("Received streaming inventory optimization request.", flush=True)

        # Validação: deve haver pelo menos um item no batch
        if len(request.items) == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("At least one inventory item must be provided.")
            return

        for item_request in request.items:
            response = self.calculate_inventory_response(item_request, context)

            # Se houver erro de validação em qualquer item, aborta o streaming
            if response is None:
                return

            print(f"Streaming recommendation for item {response.item_id}", flush=True)

            yield response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    inventory_pb2_grpc.add_InventoryOptimizationServicer_to_server(
        InventoryOptimizationService(),
        server
    )


    # Configura o servidor gRPC e expõe a porta 50051
    server.add_insecure_port("[::]:50051")
    server.start()

    print("Inventory Optimization gRPC server running on port 50051...", flush=True)

    # Bloqueia o processo principal até o servidor encerrar
    server.wait_for_termination()


if __name__ == "__main__":
    serve()