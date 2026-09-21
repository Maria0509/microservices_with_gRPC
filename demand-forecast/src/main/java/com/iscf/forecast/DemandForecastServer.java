package com.iscf.forecast;

import io.grpc.Server;
import io.grpc.ServerBuilder;

import java.io.IOException;

public class DemandForecastServer {

    public static void main(String[] args) throws IOException, InterruptedException {
        int port = 50052;

        Server server = ServerBuilder
                .forPort(port)
                .addService(new DemandForecastServiceImpl())
                .build();

        server.start();

        System.out.println("Demand Forecast gRPC server running on port " + port + "...");

        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            System.out.println("Shutting down Demand Forecast server...");
            server.shutdown();
        }));

        server.awaitTermination();
    }
}