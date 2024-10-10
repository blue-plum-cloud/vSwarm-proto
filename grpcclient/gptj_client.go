package grpcclient

import (
	"context"

	pb "github.com/blue-plum-cloud/vSwarm-proto/proto/gptj"
	log "github.com/sirupsen/logrus"
)

type GptJGenerator struct {
	GeneratorBase
}

func (g *GptJGenerator) Next(isROI bool, numCalls int32) Input {
	var pkt = g.defaultInput
	pkt.NumCalls = numCalls
	switch g.GeneratorBase.generator {
	case Unique:
		pkt.Value = "false"
	case Linear:
		pkt.Value = "false"
	case Random:
		pkt.Value = "true"
	}
	pkt.isROI = isROI
	return pkt
}

type GptJClient struct {
	ClientBase
	client pb.GptJBenchmarkClient
}

func (c *GptJClient) GetGenerator() Generator {
	return new(GptJGenerator)
}

func (c *GptJClient) Init(ctx context.Context, ip, port string) error {
	log.Printf("Connect to: %s:%s\n", ip, port)
	err := c.Connect(ctx, ip, port)
	if err != nil {
		return err
	}
	c.client = pb.NewGptJBenchmarkClient(c.conn)
	return nil
}

func (c *GptJClient) Request(ctx context.Context, req Input) (string, error) {
	r, err := c.client.GetBenchmark(ctx, &pb.GptJBenchmarkRequest{Regenerate: req.Value})
	if err != nil {
		return "", err
	}
	return r.GetLatencyInfo(), nil
}
