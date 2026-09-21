package com.iscf.forecast;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.54.2)",
    comments = "Source: demand_forecast.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class DemandForecastGrpc {

  private DemandForecastGrpc() {}

  public static final String SERVICE_NAME = "forecast.DemandForecast";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<com.iscf.forecast.DemandForecastRequest,
      com.iscf.forecast.DemandForecastResponse> getPredictDemandMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "PredictDemand",
      requestType = com.iscf.forecast.DemandForecastRequest.class,
      responseType = com.iscf.forecast.DemandForecastResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<com.iscf.forecast.DemandForecastRequest,
      com.iscf.forecast.DemandForecastResponse> getPredictDemandMethod() {
    io.grpc.MethodDescriptor<com.iscf.forecast.DemandForecastRequest, com.iscf.forecast.DemandForecastResponse> getPredictDemandMethod;
    if ((getPredictDemandMethod = DemandForecastGrpc.getPredictDemandMethod) == null) {
      synchronized (DemandForecastGrpc.class) {
        if ((getPredictDemandMethod = DemandForecastGrpc.getPredictDemandMethod) == null) {
          DemandForecastGrpc.getPredictDemandMethod = getPredictDemandMethod =
              io.grpc.MethodDescriptor.<com.iscf.forecast.DemandForecastRequest, com.iscf.forecast.DemandForecastResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "PredictDemand"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  com.iscf.forecast.DemandForecastRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  com.iscf.forecast.DemandForecastResponse.getDefaultInstance()))
              .setSchemaDescriptor(new DemandForecastMethodDescriptorSupplier("PredictDemand"))
              .build();
        }
      }
    }
    return getPredictDemandMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static DemandForecastStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<DemandForecastStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<DemandForecastStub>() {
        @java.lang.Override
        public DemandForecastStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new DemandForecastStub(channel, callOptions);
        }
      };
    return DemandForecastStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static DemandForecastBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<DemandForecastBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<DemandForecastBlockingStub>() {
        @java.lang.Override
        public DemandForecastBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new DemandForecastBlockingStub(channel, callOptions);
        }
      };
    return DemandForecastBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static DemandForecastFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<DemandForecastFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<DemandForecastFutureStub>() {
        @java.lang.Override
        public DemandForecastFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new DemandForecastFutureStub(channel, callOptions);
        }
      };
    return DemandForecastFutureStub.newStub(factory, channel);
  }

  /**
   */
  public interface AsyncService {

    /**
     */
    default void predictDemand(com.iscf.forecast.DemandForecastRequest request,
        io.grpc.stub.StreamObserver<com.iscf.forecast.DemandForecastResponse> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getPredictDemandMethod(), responseObserver);
    }
  }

  /**
   * Base class for the server implementation of the service DemandForecast.
   */
  public static abstract class DemandForecastImplBase
      implements io.grpc.BindableService, AsyncService {

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return DemandForecastGrpc.bindService(this);
    }
  }

  /**
   * A stub to allow clients to do asynchronous rpc calls to service DemandForecast.
   */
  public static final class DemandForecastStub
      extends io.grpc.stub.AbstractAsyncStub<DemandForecastStub> {
    private DemandForecastStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected DemandForecastStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new DemandForecastStub(channel, callOptions);
    }

    /**
     */
    public void predictDemand(com.iscf.forecast.DemandForecastRequest request,
        io.grpc.stub.StreamObserver<com.iscf.forecast.DemandForecastResponse> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getPredictDemandMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * A stub to allow clients to do synchronous rpc calls to service DemandForecast.
   */
  public static final class DemandForecastBlockingStub
      extends io.grpc.stub.AbstractBlockingStub<DemandForecastBlockingStub> {
    private DemandForecastBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected DemandForecastBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new DemandForecastBlockingStub(channel, callOptions);
    }

    /**
     */
    public com.iscf.forecast.DemandForecastResponse predictDemand(com.iscf.forecast.DemandForecastRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getPredictDemandMethod(), getCallOptions(), request);
    }
  }

  /**
   * A stub to allow clients to do ListenableFuture-style rpc calls to service DemandForecast.
   */
  public static final class DemandForecastFutureStub
      extends io.grpc.stub.AbstractFutureStub<DemandForecastFutureStub> {
    private DemandForecastFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected DemandForecastFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new DemandForecastFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<com.iscf.forecast.DemandForecastResponse> predictDemand(
        com.iscf.forecast.DemandForecastRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getPredictDemandMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_PREDICT_DEMAND = 0;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final AsyncService serviceImpl;
    private final int methodId;

    MethodHandlers(AsyncService serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_PREDICT_DEMAND:
          serviceImpl.predictDemand((com.iscf.forecast.DemandForecastRequest) request,
              (io.grpc.stub.StreamObserver<com.iscf.forecast.DemandForecastResponse>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  public static final io.grpc.ServerServiceDefinition bindService(AsyncService service) {
    return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
        .addMethod(
          getPredictDemandMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              com.iscf.forecast.DemandForecastRequest,
              com.iscf.forecast.DemandForecastResponse>(
                service, METHODID_PREDICT_DEMAND)))
        .build();
  }

  private static abstract class DemandForecastBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    DemandForecastBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return com.iscf.forecast.DemandForecastProto.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("DemandForecast");
    }
  }

  private static final class DemandForecastFileDescriptorSupplier
      extends DemandForecastBaseDescriptorSupplier {
    DemandForecastFileDescriptorSupplier() {}
  }

  private static final class DemandForecastMethodDescriptorSupplier
      extends DemandForecastBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    DemandForecastMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (DemandForecastGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new DemandForecastFileDescriptorSupplier())
              .addMethod(getPredictDemandMethod())
              .build();
        }
      }
    }
    return result;
  }
}
