import grpc

import inventory_pb2
import inventory_pb2_grpc


# Arquivo: inventory/client.py
# Descrição: Cliente de teste para o serviço de otimização de inventário.
# Finalidade:
# - Montar cenários de teste (válidos e inválidos)
# - Enviar requisições ao método `OptimizeInventory` e imprimir as respostas
def print_response(response):
    # Função utilitária para formatar a saída da resposta gRPC
    print("Response from Inventory Optimization Service:")
    print(f"Item ID: {response.item_id}")
    print(f"Reorder Quantity: {response.reorder_quantity}")
    print(
        "Inventory Adjustment Action:",
        inventory_pb2.InventoryAdjustmentAction.Name(
            response.inventory_adjustment_action
        )
    )
    print(f"Explanation Message: {response.explanation_message}")


def run():
    # Cria um canal inseguro (para execução local) apontando para o servidor gRPC
    channel = grpc.insecure_channel("localhost:50051")
    stub = inventory_pb2_grpc.InventoryOptimizationStub(channel)

    # Lista de cenários que exercitam diferentes caminhos de validação e lógica
    test_scenarios = [
        {
            "name": "Scenario 1 - Low stock, reorder needed",
            "request": inventory_pb2.InventoryRequest(
                item_id="ITEM001",
                current_stock=20,
                predicted_demand=50,
                reorder_level=10,
                safety_stock=5,
                supplier_lead_time=2
            )
        },
        {
            "name": "Scenario 2 - Stock is sufficient, no action needed",
            "request": inventory_pb2.InventoryRequest(
                item_id="ITEM002",
                current_stock=80,
                predicted_demand=50,
                reorder_level=10,
                safety_stock=5,
                supplier_lead_time=1
            )
        },
        {
            "name": "Scenario 3 - Stock is too high, scale down",
            "request": inventory_pb2.InventoryRequest(
                item_id="ITEM003",
                current_stock=200,
                predicted_demand=50,
                reorder_level=10,
                safety_stock=5,
                supplier_lead_time=1
            )
        },
        {
            "name": "Scenario 4 - Invalid negative stock",
            "request": inventory_pb2.InventoryRequest(
                item_id="ITEM004",
                current_stock=-10,
                predicted_demand=50,
                reorder_level=10,
                safety_stock=5,
                supplier_lead_time=1
            )
        },
        {
            "name": "Scenario 5 - Invalid empty item ID",
            "request": inventory_pb2.InventoryRequest(
                item_id="",
                current_stock=20,
                predicted_demand=50,
                reorder_level=10,
                safety_stock=5,
                supplier_lead_time=1
            )
        }
    ]

    for scenario in test_scenarios:
        print("\n" + "=" * 70)
        print(scenario["name"])
        print("=" * 70)

        try:
            # Chamada RPC síncrona para obter a recomendação
            response = stub.OptimizeInventory(scenario["request"])
            print_response(response)

        except grpc.RpcError as e:
            # Tratamento básico de erros gRPC para diagnóstico
            print("gRPC error received from server:")
            print(f"Status code: {e.code()}")
            print(f"Details: {e.details()}")


if __name__ == "__main__":
    run()