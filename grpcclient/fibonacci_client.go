package grpcclient

import (
	"context"
	"fmt"
	"math/rand"

	pb "github.com/blue-plum-cloud/vSwarm-proto/proto/fibonacci"
)

type FibonacciGenerator struct {
	GeneratorBase
}

func (g *FibonacciGenerator) Next(isROI bool, numCalls int32) Input {
	var pkt = g.defaultInput
	pkt.isROI = isROI
	pkt.NumCalls = numCalls
	switch g.GeneratorBase.generator {
	case Unique:

	case Linear:
		pkt.Value = fmt.Sprintf("%d", g.Increment())

	case Random:
		var fibNum int
		if g.lowerBound == g.upperBound {
			fibNum = g.lowerBound
		} else {
			fibNum = rand.Intn(g.upperBound-g.lowerBound) + g.lowerBound
		}
		pkt.Value = fmt.Sprintf("%d", fibNum)
	}
	return pkt
}

func (c *FibonacciClient) GetGenerator() Generator {
	return new(FibonacciGenerator)
}

type FibonacciClient struct {
	ClientBase
	client pb.GreeterClient
}

func (c *FibonacciClient) Init(ctx context.Context, ip, port string) error {
	err := c.Connect(ctx, ip, port)
	if err != nil {
		return err
	}
	c.client = pb.NewGreeterClient(c.conn)
	return nil
}

func (c *FibonacciClient) Request(ctx context.Context, req Input) (string, error) {
	var fibonacciMessage = req.Value
	r, err := c.client.SayHello(ctx, &pb.HelloRequest{Name: fibonacciMessage, IsROI: req.isROI})
	if err != nil {
		return "", err
	}
	return r.GetMessage(), nil
}
