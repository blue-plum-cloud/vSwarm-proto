package grpcclient

import (
	"context"

	pb "github.com/blue-plum-cloud/vSwarm-proto/proto/video_analytics_standalone"
)

type VideoAnalyticsGenerator struct {
	GeneratorBase
}

func (g *VideoAnalyticsGenerator) Next(isROI bool, numCalls int32) Input {
	var pkt = g.defaultInput
	pkt.isROI = isROI
	pkt.NumCalls = numCalls
	return pkt
}

func (c *VideoAnalyticsClient) GetGenerator() Generator {
	return new(VideoAnalyticsGenerator)
}

type VideoAnalyticsClient struct {
	ClientBase
	client pb.VideoAnalyticsClient
}

func (c *VideoAnalyticsClient) Init(ctx context.Context, ip, port string) error {
	err := c.Connect(ctx, ip, port)
	if err != nil {
		return err
	}
	c.client = pb.NewVideoAnalyticsClient(c.conn)
	return nil
}

func (c *VideoAnalyticsClient) Request(ctx context.Context, req Input) (string, error) {
	r, err := c.client.ObjectDetection(ctx, &pb.SendVideo{Name: req.Value})
	if err != nil {
		return "", err
	}
	return r.GetMessage(), nil
}
