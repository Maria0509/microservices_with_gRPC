FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY demand_forecast_pb2.py .
COPY demand_forecast_pb2_grpc.py .
COPY inventory_pb2.py .
COPY inventory_pb2_grpc.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
