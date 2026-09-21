FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY inventory_pb2.py .
COPY inventory_pb2_grpc.py .

EXPOSE 50051

CMD ["python", "-u", "server.py"]