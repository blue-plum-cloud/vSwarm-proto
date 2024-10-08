// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.31.0
// 	protoc        v4.25.0
// source: proto/hotel_reserv/geo/geo.proto

package geo

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// The latitude and longitude of the current location.
type Request struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Lat      float32 `protobuf:"fixed32,1,opt,name=lat,proto3" json:"lat,omitempty"`
	Lon      float32 `protobuf:"fixed32,2,opt,name=lon,proto3" json:"lon,omitempty"`
	IsROI    bool    `protobuf:"varint,3,opt,name=isROI,proto3" json:"isROI,omitempty"`
	NumCalls int32   `protobuf:"varint,4,opt,name=num_calls,json=numCalls,proto3" json:"num_calls,omitempty"`
}

func (x *Request) Reset() {
	*x = Request{}
	if protoimpl.UnsafeEnabled {
		mi := &file_proto_hotel_reserv_geo_geo_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Request) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Request) ProtoMessage() {}

func (x *Request) ProtoReflect() protoreflect.Message {
	mi := &file_proto_hotel_reserv_geo_geo_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Request.ProtoReflect.Descriptor instead.
func (*Request) Descriptor() ([]byte, []int) {
	return file_proto_hotel_reserv_geo_geo_proto_rawDescGZIP(), []int{0}
}

func (x *Request) GetLat() float32 {
	if x != nil {
		return x.Lat
	}
	return 0
}

func (x *Request) GetLon() float32 {
	if x != nil {
		return x.Lon
	}
	return 0
}

func (x *Request) GetIsROI() bool {
	if x != nil {
		return x.IsROI
	}
	return false
}

func (x *Request) GetNumCalls() int32 {
	if x != nil {
		return x.NumCalls
	}
	return 0
}

type Result struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	HotelIds []string `protobuf:"bytes,1,rep,name=hotelIds,proto3" json:"hotelIds,omitempty"`
}

func (x *Result) Reset() {
	*x = Result{}
	if protoimpl.UnsafeEnabled {
		mi := &file_proto_hotel_reserv_geo_geo_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Result) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Result) ProtoMessage() {}

func (x *Result) ProtoReflect() protoreflect.Message {
	mi := &file_proto_hotel_reserv_geo_geo_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Result.ProtoReflect.Descriptor instead.
func (*Result) Descriptor() ([]byte, []int) {
	return file_proto_hotel_reserv_geo_geo_proto_rawDescGZIP(), []int{1}
}

func (x *Result) GetHotelIds() []string {
	if x != nil {
		return x.HotelIds
	}
	return nil
}

var File_proto_hotel_reserv_geo_geo_proto protoreflect.FileDescriptor

var file_proto_hotel_reserv_geo_geo_proto_rawDesc = []byte{
	0x0a, 0x20, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2f, 0x68, 0x6f, 0x74, 0x65, 0x6c, 0x5f, 0x72, 0x65,
	0x73, 0x65, 0x72, 0x76, 0x2f, 0x67, 0x65, 0x6f, 0x2f, 0x67, 0x65, 0x6f, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x12, 0x03, 0x67, 0x65, 0x6f, 0x22, 0x60, 0x0a, 0x07, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x12, 0x10, 0x0a, 0x03, 0x6c, 0x61, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x02, 0x52,
	0x03, 0x6c, 0x61, 0x74, 0x12, 0x10, 0x0a, 0x03, 0x6c, 0x6f, 0x6e, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x02, 0x52, 0x03, 0x6c, 0x6f, 0x6e, 0x12, 0x14, 0x0a, 0x05, 0x69, 0x73, 0x52, 0x4f, 0x49, 0x18,
	0x03, 0x20, 0x01, 0x28, 0x08, 0x52, 0x05, 0x69, 0x73, 0x52, 0x4f, 0x49, 0x12, 0x1b, 0x0a, 0x09,
	0x6e, 0x75, 0x6d, 0x5f, 0x63, 0x61, 0x6c, 0x6c, 0x73, 0x18, 0x04, 0x20, 0x01, 0x28, 0x05, 0x52,
	0x08, 0x6e, 0x75, 0x6d, 0x43, 0x61, 0x6c, 0x6c, 0x73, 0x22, 0x24, 0x0a, 0x06, 0x52, 0x65, 0x73,
	0x75, 0x6c, 0x74, 0x12, 0x1a, 0x0a, 0x08, 0x68, 0x6f, 0x74, 0x65, 0x6c, 0x49, 0x64, 0x73, 0x18,
	0x01, 0x20, 0x03, 0x28, 0x09, 0x52, 0x08, 0x68, 0x6f, 0x74, 0x65, 0x6c, 0x49, 0x64, 0x73, 0x32,
	0x2a, 0x0a, 0x03, 0x47, 0x65, 0x6f, 0x12, 0x23, 0x0a, 0x06, 0x4e, 0x65, 0x61, 0x72, 0x62, 0x79,
	0x12, 0x0c, 0x2e, 0x67, 0x65, 0x6f, 0x2e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x0b,
	0x2e, 0x67, 0x65, 0x6f, 0x2e, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x42, 0x12, 0x5a, 0x10, 0x68,
	0x6f, 0x74, 0x65, 0x6c, 0x5f, 0x72, 0x65, 0x73, 0x65, 0x72, 0x76, 0x2f, 0x67, 0x65, 0x6f, 0x62,
	0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_proto_hotel_reserv_geo_geo_proto_rawDescOnce sync.Once
	file_proto_hotel_reserv_geo_geo_proto_rawDescData = file_proto_hotel_reserv_geo_geo_proto_rawDesc
)

func file_proto_hotel_reserv_geo_geo_proto_rawDescGZIP() []byte {
	file_proto_hotel_reserv_geo_geo_proto_rawDescOnce.Do(func() {
		file_proto_hotel_reserv_geo_geo_proto_rawDescData = protoimpl.X.CompressGZIP(file_proto_hotel_reserv_geo_geo_proto_rawDescData)
	})
	return file_proto_hotel_reserv_geo_geo_proto_rawDescData
}

var file_proto_hotel_reserv_geo_geo_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_proto_hotel_reserv_geo_geo_proto_goTypes = []interface{}{
	(*Request)(nil), // 0: geo.Request
	(*Result)(nil),  // 1: geo.Result
}
var file_proto_hotel_reserv_geo_geo_proto_depIdxs = []int32{
	0, // 0: geo.Geo.Nearby:input_type -> geo.Request
	1, // 1: geo.Geo.Nearby:output_type -> geo.Result
	1, // [1:2] is the sub-list for method output_type
	0, // [0:1] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_proto_hotel_reserv_geo_geo_proto_init() }
func file_proto_hotel_reserv_geo_geo_proto_init() {
	if File_proto_hotel_reserv_geo_geo_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_proto_hotel_reserv_geo_geo_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Request); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_proto_hotel_reserv_geo_geo_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Result); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_proto_hotel_reserv_geo_geo_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_proto_hotel_reserv_geo_geo_proto_goTypes,
		DependencyIndexes: file_proto_hotel_reserv_geo_geo_proto_depIdxs,
		MessageInfos:      file_proto_hotel_reserv_geo_geo_proto_msgTypes,
	}.Build()
	File_proto_hotel_reserv_geo_geo_proto = out.File
	file_proto_hotel_reserv_geo_geo_proto_rawDesc = nil
	file_proto_hotel_reserv_geo_geo_proto_goTypes = nil
	file_proto_hotel_reserv_geo_geo_proto_depIdxs = nil
}
