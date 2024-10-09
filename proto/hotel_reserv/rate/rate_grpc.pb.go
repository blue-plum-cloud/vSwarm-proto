// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             v4.25.0
// source: proto/hotel_reserv/rate/rate.proto

package rate

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

const (
	Rate_GetRates_FullMethodName = "/rate.Rate/GetRates"
)

// RateClient is the client API for Rate service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type RateClient interface {
	// GetRates returns rate codes for hotels for a given date range
	GetRates(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Result, error)
}

type rateClient struct {
	cc grpc.ClientConnInterface
}

func NewRateClient(cc grpc.ClientConnInterface) RateClient {
	return &rateClient{cc}
}

func (c *rateClient) GetRates(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Result, error) {
	out := new(Result)
	err := c.cc.Invoke(ctx, Rate_GetRates_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// RateServer is the server API for Rate service.
// All implementations must embed UnimplementedRateServer
// for forward compatibility
type RateServer interface {
	// GetRates returns rate codes for hotels for a given date range
	GetRates(context.Context, *Request) (*Result, error)
	mustEmbedUnimplementedRateServer()
}

// UnimplementedRateServer must be embedded to have forward compatible implementations.
type UnimplementedRateServer struct {
}

func (UnimplementedRateServer) GetRates(context.Context, *Request) (*Result, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetRates not implemented")
}
func (UnimplementedRateServer) mustEmbedUnimplementedRateServer() {}

// UnsafeRateServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to RateServer will
// result in compilation errors.
type UnsafeRateServer interface {
	mustEmbedUnimplementedRateServer()
}

func RegisterRateServer(s grpc.ServiceRegistrar, srv RateServer) {
	s.RegisterService(&Rate_ServiceDesc, srv)
}

func _Rate_GetRates_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(RateServer).GetRates(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Rate_GetRates_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(RateServer).GetRates(ctx, req.(*Request))
	}
	return interceptor(ctx, in, info, handler)
}

// Rate_ServiceDesc is the grpc.ServiceDesc for Rate service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Rate_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "rate.Rate",
	HandlerType: (*RateServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetRates",
			Handler:    _Rate_GetRates_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "proto/hotel_reserv/rate/rate.proto",
}
