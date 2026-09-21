package com.iscf.forecast;

import io.grpc.Status;
import io.grpc.stub.StreamObserver;

public class DemandForecastServiceImpl extends DemandForecastGrpc.DemandForecastImplBase {

    @Override
    public void predictDemand(
            DemandForecastRequest request,
            StreamObserver<DemandForecastResponse> responseObserver
    ) {
        String itemId = request.getItemId();
        int forecastHorizon = request.getForecastHorizon();
        String warehouseId = request.getWarehouseId();

        if (itemId == null || itemId.isEmpty()) {
            responseObserver.onError(
                    Status.INVALID_ARGUMENT
                            .withDescription("Item ID cannot be empty.")
                            .asRuntimeException()
            );
            return;
        }

        if (warehouseId == null || warehouseId.isEmpty()) {
            responseObserver.onError(
                    Status.INVALID_ARGUMENT
                            .withDescription("Warehouse ID cannot be empty.")
                            .asRuntimeException()
            );
            return;
        }

        if (forecastHorizon <= 0) {
            responseObserver.onError(
                    Status.INVALID_ARGUMENT
                            .withDescription("Forecast horizon must be greater than zero.")
                            .asRuntimeException()
            );
            return;
        }

        if (request.getHistoricalDemandCount() == 0) {
            responseObserver.onError(
                    Status.INVALID_ARGUMENT
                            .withDescription("Historical demand values cannot be empty.")
                            .asRuntimeException()
            );
            return;
        }

        int sum = 0;

        for (int value : request.getHistoricalDemandList()) {
            if (value < 0) {
                responseObserver.onError(
                        Status.INVALID_ARGUMENT
                                .withDescription("Historical demand values must be non-negative.")
                                .asRuntimeException()
                );
                return;
            }

            sum += value;
        }

        double average = (double) sum / request.getHistoricalDemandCount();

        int predictedDemand = (int) Math.round(average * forecastHorizon);

        double confidence = calculateConfidence(request);

        DemandForecastResponse response = DemandForecastResponse.newBuilder()
                .setItemId(itemId)
                .setPredictedDemand(predictedDemand)
                .setForecastConfidence(confidence)
                .setForecastHorizon(forecastHorizon)
                .build();

        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }

    private double calculateConfidence(DemandForecastRequest request) {
        int count = request.getHistoricalDemandCount();

        if (count >= 5) {
            return 0.90;
        } else if (count >= 3) {
            return 0.75;
        } else {
            return 0.60;
        }
    }
}