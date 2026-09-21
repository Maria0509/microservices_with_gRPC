# ISCF Lab 3 - Run Instructions

## Requirements

- Docker
- Docker Compose

## Run

From the project root folder:

```bash
cd /mnt/hgfs/iscf_trab3
docker compose up --build

If needed:

docker-compose up --build
Access

Web App:

http://localhost:8080

FastAPI docs:

http://localhost:8000/docs

Ports
8080  - Web App
8000  - FastAPI
50052 - Demand Forecasting gRPC Service
50051 - Inventory Optimization gRPC Service