import grpc

import inventory_pb2
import inventory_pb2_grpc


# Arquivo: inventory/streaming_client.py
# Descrição: Cliente que demonstra chamadas server-streaming ao serviço de inventário.
# O cliente envia um `InventoryBatchRequest` com múltiplos itens e itera sobre as respostas
# geradas pelo servidor (cada `InventoryResponse` é enviada pelo servidor usando streaming).
def run():
    # Cria o canal gRPC local e o stub para chamar os métodos remotos
    channel = grpc.insecure_channel("localhost:50051")
    stub = inventory_pb2_grpc.InventoryOptimizationStub(channel)

    # Monta um batch com múltiplos itens para demonstrar streaming
    batch_request = inventory_pb2.InventoryBatchRequest(
        items=[
            inventory_pb2.InventoryRequest(
                item_id="ITEM001",
                current_stock=20,
                predicted_demand=50,
                reorder_level=10,
                safety_stock=5,
                supplier_lead_time=2
            ),
            inventory_pb2.InventoryRequest(
                item_id="ITEM002",
                current_stock=80,
                predicted_demand=50,
                reorder_level=10,
                safety_stock=5,
                supplier_lead_time=1
            ),
            inventory_pb2.InventoryRequest(
                item_id="ITEM003",
                current_stock=200,
                predicted_demand=50,
                reorder_level=10,
                safety_stock=5,
                supplier_lead_time=1
            )
        ]
    )

    try:
        print("Requesting inventory recommendations using server streaming...\n")

        # Chamada ao método streaming do servidor; `responses` é um iterador/generator
        responses = stub.OptimizeInventoryStream(batch_request)

        for response in responses:
            # Converte o enum da resposta para o nome legível
            action_name = inventory_pb2.InventoryAdjustmentAction.Name(
                response.inventory_adjustment_action
            )

            # Imprime de forma legível cada recomendação recebida
            print("=" * 60)
            print(f"Item ID: {response.item_id}")
            print(f"Reorder Quantity: {response.reorder_quantity}")
            print(f"Inventory Action: {action_name}")
            print(f"Explanation: {response.explanation_message}")

    except grpc.RpcError as e:
        # Tratamento básico de erro de streaming para diagnóstico
        print("gRPC streaming error:")
        print(f"Status code: {e.code()}")
        print(f"Details: {e.details()}")


if __name__ == "__main__":
    run()