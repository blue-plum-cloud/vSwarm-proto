# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/hipstershop/demo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cproto/hipstershop/demo.proto\x12\x0bhipstershop\"0\n\x08\x43\x61rtItem\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"F\n\x0e\x41\x64\x64ItemRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12#\n\x04item\x18\x02 \x01(\x0b\x32\x15.hipstershop.CartItem\"#\n\x10\x45mptyCartRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"!\n\x0eGetCartRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"=\n\x04\x43\x61rt\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12$\n\x05items\x18\x02 \x03(\x0b\x32\x15.hipstershop.CartItem\"\x07\n\x05\x45mpty\"B\n\x1aListRecommendationsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x13\n\x0bproduct_ids\x18\x02 \x03(\t\"2\n\x1bListRecommendationsResponse\x12\x13\n\x0bproduct_ids\x18\x01 \x03(\t\"\x84\x01\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07picture\x18\x04 \x01(\t\x12%\n\tprice_usd\x18\x05 \x01(\x0b\x32\x12.hipstershop.Money\x12\x12\n\ncategories\x18\x06 \x03(\t\">\n\x14ListProductsResponse\x12&\n\x08products\x18\x01 \x03(\x0b\x32\x14.hipstershop.Product\"\x1f\n\x11GetProductRequest\x12\n\n\x02id\x18\x01 \x01(\t\"&\n\x15SearchProductsRequest\x12\r\n\x05query\x18\x01 \x01(\t\"?\n\x16SearchProductsResponse\x12%\n\x07results\x18\x01 \x03(\x0b\x32\x14.hipstershop.Product\"^\n\x0fGetQuoteRequest\x12%\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x14.hipstershop.Address\x12$\n\x05items\x18\x02 \x03(\x0b\x32\x15.hipstershop.CartItem\"8\n\x10GetQuoteResponse\x12$\n\x08\x63ost_usd\x18\x01 \x01(\x0b\x32\x12.hipstershop.Money\"_\n\x10ShipOrderRequest\x12%\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x14.hipstershop.Address\x12$\n\x05items\x18\x02 \x03(\x0b\x32\x15.hipstershop.CartItem\"(\n\x11ShipOrderResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\"a\n\x07\x41\x64\x64ress\x12\x16\n\x0estreet_address\x18\x01 \x01(\t\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x04 \x01(\t\x12\x10\n\x08zip_code\x18\x05 \x01(\x05\"<\n\x05Money\x12\x15\n\rcurrency_code\x18\x01 \x01(\t\x12\r\n\x05units\x18\x02 \x01(\x03\x12\r\n\x05nanos\x18\x03 \x01(\x05\"8\n\x1eGetSupportedCurrenciesResponse\x12\x16\n\x0e\x63urrency_codes\x18\x01 \x03(\t\"N\n\x19\x43urrencyConversionRequest\x12 \n\x04\x66rom\x18\x01 \x01(\x0b\x32\x12.hipstershop.Money\x12\x0f\n\x07to_code\x18\x02 \x01(\t\"\x90\x01\n\x0e\x43reditCardInfo\x12\x1a\n\x12\x63redit_card_number\x18\x01 \x01(\t\x12\x17\n\x0f\x63redit_card_cvv\x18\x02 \x01(\x05\x12#\n\x1b\x63redit_card_expiration_year\x18\x03 \x01(\x05\x12$\n\x1c\x63redit_card_expiration_month\x18\x04 \x01(\x05\"e\n\rChargeRequest\x12\"\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x12.hipstershop.Money\x12\x30\n\x0b\x63redit_card\x18\x02 \x01(\x0b\x32\x1b.hipstershop.CreditCardInfo\"(\n\x0e\x43hargeResponse\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\"R\n\tOrderItem\x12#\n\x04item\x18\x01 \x01(\x0b\x32\x15.hipstershop.CartItem\x12 \n\x04\x63ost\x18\x02 \x01(\x0b\x32\x12.hipstershop.Money\"\xbf\x01\n\x0bOrderResult\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x1c\n\x14shipping_tracking_id\x18\x02 \x01(\t\x12)\n\rshipping_cost\x18\x03 \x01(\x0b\x32\x12.hipstershop.Money\x12.\n\x10shipping_address\x18\x04 \x01(\x0b\x32\x14.hipstershop.Address\x12%\n\x05items\x18\x05 \x03(\x0b\x32\x16.hipstershop.OrderItem\"V\n\x1cSendOrderConfirmationRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\'\n\x05order\x18\x02 \x01(\x0b\x32\x18.hipstershop.OrderResult\"\xa3\x01\n\x11PlaceOrderRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x15\n\ruser_currency\x18\x02 \x01(\t\x12%\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x14.hipstershop.Address\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x30\n\x0b\x63redit_card\x18\x06 \x01(\x0b\x32\x1b.hipstershop.CreditCardInfo\"=\n\x12PlaceOrderResponse\x12\'\n\x05order\x18\x01 \x01(\x0b\x32\x18.hipstershop.OrderResult\"!\n\tAdRequest\x12\x14\n\x0c\x63ontext_keys\x18\x01 \x03(\t\"*\n\nAdResponse\x12\x1c\n\x03\x61\x64s\x18\x01 \x03(\x0b\x32\x0f.hipstershop.Ad\"(\n\x02\x41\x64\x12\x14\n\x0credirect_url\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t2\xca\x01\n\x0b\x43\x61rtService\x12<\n\x07\x41\x64\x64Item\x12\x1b.hipstershop.AddItemRequest\x1a\x12.hipstershop.Empty\"\x00\x12;\n\x07GetCart\x12\x1b.hipstershop.GetCartRequest\x1a\x11.hipstershop.Cart\"\x00\x12@\n\tEmptyCart\x12\x1d.hipstershop.EmptyCartRequest\x1a\x12.hipstershop.Empty\"\x00\x32\x83\x01\n\x15RecommendationService\x12j\n\x13ListRecommendations\x12\'.hipstershop.ListRecommendationsRequest\x1a(.hipstershop.ListRecommendationsResponse\"\x00\x32\x83\x02\n\x15ProductCatalogService\x12G\n\x0cListProducts\x12\x12.hipstershop.Empty\x1a!.hipstershop.ListProductsResponse\"\x00\x12\x44\n\nGetProduct\x12\x1e.hipstershop.GetProductRequest\x1a\x14.hipstershop.Product\"\x00\x12[\n\x0eSearchProducts\x12\".hipstershop.SearchProductsRequest\x1a#.hipstershop.SearchProductsResponse\"\x00\x32\xaa\x01\n\x0fShippingService\x12I\n\x08GetQuote\x12\x1c.hipstershop.GetQuoteRequest\x1a\x1d.hipstershop.GetQuoteResponse\"\x00\x12L\n\tShipOrder\x12\x1d.hipstershop.ShipOrderRequest\x1a\x1e.hipstershop.ShipOrderResponse\"\x00\x32\xb7\x01\n\x0f\x43urrencyService\x12[\n\x16GetSupportedCurrencies\x12\x12.hipstershop.Empty\x1a+.hipstershop.GetSupportedCurrenciesResponse\"\x00\x12G\n\x07\x43onvert\x12&.hipstershop.CurrencyConversionRequest\x1a\x12.hipstershop.Money\"\x00\x32U\n\x0ePaymentService\x12\x43\n\x06\x43harge\x12\x1a.hipstershop.ChargeRequest\x1a\x1b.hipstershop.ChargeResponse\"\x00\x32h\n\x0c\x45mailService\x12X\n\x15SendOrderConfirmation\x12).hipstershop.SendOrderConfirmationRequest\x1a\x12.hipstershop.Empty\"\x00\x32\x62\n\x0f\x43heckoutService\x12O\n\nPlaceOrder\x12\x1e.hipstershop.PlaceOrderRequest\x1a\x1f.hipstershop.PlaceOrderResponse\"\x00\x32H\n\tAdService\x12;\n\x06GetAds\x12\x16.hipstershop.AdRequest\x1a\x17.hipstershop.AdResponse\"\x00\x42\x34Z2github.com/ease-lab/vSwarm-proto/proto/hipstershopb\x06proto3')



_CARTITEM = DESCRIPTOR.message_types_by_name['CartItem']
_ADDITEMREQUEST = DESCRIPTOR.message_types_by_name['AddItemRequest']
_EMPTYCARTREQUEST = DESCRIPTOR.message_types_by_name['EmptyCartRequest']
_GETCARTREQUEST = DESCRIPTOR.message_types_by_name['GetCartRequest']
_CART = DESCRIPTOR.message_types_by_name['Cart']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_LISTRECOMMENDATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListRecommendationsRequest']
_LISTRECOMMENDATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListRecommendationsResponse']
_PRODUCT = DESCRIPTOR.message_types_by_name['Product']
_LISTPRODUCTSRESPONSE = DESCRIPTOR.message_types_by_name['ListProductsResponse']
_GETPRODUCTREQUEST = DESCRIPTOR.message_types_by_name['GetProductRequest']
_SEARCHPRODUCTSREQUEST = DESCRIPTOR.message_types_by_name['SearchProductsRequest']
_SEARCHPRODUCTSRESPONSE = DESCRIPTOR.message_types_by_name['SearchProductsResponse']
_GETQUOTEREQUEST = DESCRIPTOR.message_types_by_name['GetQuoteRequest']
_GETQUOTERESPONSE = DESCRIPTOR.message_types_by_name['GetQuoteResponse']
_SHIPORDERREQUEST = DESCRIPTOR.message_types_by_name['ShipOrderRequest']
_SHIPORDERRESPONSE = DESCRIPTOR.message_types_by_name['ShipOrderResponse']
_ADDRESS = DESCRIPTOR.message_types_by_name['Address']
_MONEY = DESCRIPTOR.message_types_by_name['Money']
_GETSUPPORTEDCURRENCIESRESPONSE = DESCRIPTOR.message_types_by_name['GetSupportedCurrenciesResponse']
_CURRENCYCONVERSIONREQUEST = DESCRIPTOR.message_types_by_name['CurrencyConversionRequest']
_CREDITCARDINFO = DESCRIPTOR.message_types_by_name['CreditCardInfo']
_CHARGEREQUEST = DESCRIPTOR.message_types_by_name['ChargeRequest']
_CHARGERESPONSE = DESCRIPTOR.message_types_by_name['ChargeResponse']
_ORDERITEM = DESCRIPTOR.message_types_by_name['OrderItem']
_ORDERRESULT = DESCRIPTOR.message_types_by_name['OrderResult']
_SENDORDERCONFIRMATIONREQUEST = DESCRIPTOR.message_types_by_name['SendOrderConfirmationRequest']
_PLACEORDERREQUEST = DESCRIPTOR.message_types_by_name['PlaceOrderRequest']
_PLACEORDERRESPONSE = DESCRIPTOR.message_types_by_name['PlaceOrderResponse']
_ADREQUEST = DESCRIPTOR.message_types_by_name['AdRequest']
_ADRESPONSE = DESCRIPTOR.message_types_by_name['AdResponse']
_AD = DESCRIPTOR.message_types_by_name['Ad']
CartItem = _reflection.GeneratedProtocolMessageType('CartItem', (_message.Message,), {
  'DESCRIPTOR' : _CARTITEM,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.CartItem)
  })
_sym_db.RegisterMessage(CartItem)

AddItemRequest = _reflection.GeneratedProtocolMessageType('AddItemRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDITEMREQUEST,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.AddItemRequest)
  })
_sym_db.RegisterMessage(AddItemRequest)

EmptyCartRequest = _reflection.GeneratedProtocolMessageType('EmptyCartRequest', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYCARTREQUEST,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.EmptyCartRequest)
  })
_sym_db.RegisterMessage(EmptyCartRequest)

GetCartRequest = _reflection.GeneratedProtocolMessageType('GetCartRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCARTREQUEST,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.GetCartRequest)
  })
_sym_db.RegisterMessage(GetCartRequest)

Cart = _reflection.GeneratedProtocolMessageType('Cart', (_message.Message,), {
  'DESCRIPTOR' : _CART,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.Cart)
  })
_sym_db.RegisterMessage(Cart)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.Empty)
  })
_sym_db.RegisterMessage(Empty)

ListRecommendationsRequest = _reflection.GeneratedProtocolMessageType('ListRecommendationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTRECOMMENDATIONSREQUEST,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.ListRecommendationsRequest)
  })
_sym_db.RegisterMessage(ListRecommendationsRequest)

ListRecommendationsResponse = _reflection.GeneratedProtocolMessageType('ListRecommendationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRECOMMENDATIONSRESPONSE,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.ListRecommendationsResponse)
  })
_sym_db.RegisterMessage(ListRecommendationsResponse)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.Product)
  })
_sym_db.RegisterMessage(Product)

ListProductsResponse = _reflection.GeneratedProtocolMessageType('ListProductsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPRODUCTSRESPONSE,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.ListProductsResponse)
  })
_sym_db.RegisterMessage(ListProductsResponse)

GetProductRequest = _reflection.GeneratedProtocolMessageType('GetProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRODUCTREQUEST,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.GetProductRequest)
  })
_sym_db.RegisterMessage(GetProductRequest)

SearchProductsRequest = _reflection.GeneratedProtocolMessageType('SearchProductsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHPRODUCTSREQUEST,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.SearchProductsRequest)
  })
_sym_db.RegisterMessage(SearchProductsRequest)

SearchProductsResponse = _reflection.GeneratedProtocolMessageType('SearchProductsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHPRODUCTSRESPONSE,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.SearchProductsResponse)
  })
_sym_db.RegisterMessage(SearchProductsResponse)

GetQuoteRequest = _reflection.GeneratedProtocolMessageType('GetQuoteRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETQUOTEREQUEST,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.GetQuoteRequest)
  })
_sym_db.RegisterMessage(GetQuoteRequest)

GetQuoteResponse = _reflection.GeneratedProtocolMessageType('GetQuoteResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETQUOTERESPONSE,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.GetQuoteResponse)
  })
_sym_db.RegisterMessage(GetQuoteResponse)

ShipOrderRequest = _reflection.GeneratedProtocolMessageType('ShipOrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHIPORDERREQUEST,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.ShipOrderRequest)
  })
_sym_db.RegisterMessage(ShipOrderRequest)

ShipOrderResponse = _reflection.GeneratedProtocolMessageType('ShipOrderResponse', (_message.Message,), {
  'DESCRIPTOR' : _SHIPORDERRESPONSE,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.ShipOrderResponse)
  })
_sym_db.RegisterMessage(ShipOrderResponse)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESS,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.Address)
  })
_sym_db.RegisterMessage(Address)

Money = _reflection.GeneratedProtocolMessageType('Money', (_message.Message,), {
  'DESCRIPTOR' : _MONEY,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.Money)
  })
_sym_db.RegisterMessage(Money)

GetSupportedCurrenciesResponse = _reflection.GeneratedProtocolMessageType('GetSupportedCurrenciesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSUPPORTEDCURRENCIESRESPONSE,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.GetSupportedCurrenciesResponse)
  })
_sym_db.RegisterMessage(GetSupportedCurrenciesResponse)

CurrencyConversionRequest = _reflection.GeneratedProtocolMessageType('CurrencyConversionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CURRENCYCONVERSIONREQUEST,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.CurrencyConversionRequest)
  })
_sym_db.RegisterMessage(CurrencyConversionRequest)

CreditCardInfo = _reflection.GeneratedProtocolMessageType('CreditCardInfo', (_message.Message,), {
  'DESCRIPTOR' : _CREDITCARDINFO,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.CreditCardInfo)
  })
_sym_db.RegisterMessage(CreditCardInfo)

ChargeRequest = _reflection.GeneratedProtocolMessageType('ChargeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHARGEREQUEST,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.ChargeRequest)
  })
_sym_db.RegisterMessage(ChargeRequest)

ChargeResponse = _reflection.GeneratedProtocolMessageType('ChargeResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHARGERESPONSE,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.ChargeResponse)
  })
_sym_db.RegisterMessage(ChargeResponse)

OrderItem = _reflection.GeneratedProtocolMessageType('OrderItem', (_message.Message,), {
  'DESCRIPTOR' : _ORDERITEM,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.OrderItem)
  })
_sym_db.RegisterMessage(OrderItem)

OrderResult = _reflection.GeneratedProtocolMessageType('OrderResult', (_message.Message,), {
  'DESCRIPTOR' : _ORDERRESULT,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.OrderResult)
  })
_sym_db.RegisterMessage(OrderResult)

SendOrderConfirmationRequest = _reflection.GeneratedProtocolMessageType('SendOrderConfirmationRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDORDERCONFIRMATIONREQUEST,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.SendOrderConfirmationRequest)
  })
_sym_db.RegisterMessage(SendOrderConfirmationRequest)

PlaceOrderRequest = _reflection.GeneratedProtocolMessageType('PlaceOrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLACEORDERREQUEST,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.PlaceOrderRequest)
  })
_sym_db.RegisterMessage(PlaceOrderRequest)

PlaceOrderResponse = _reflection.GeneratedProtocolMessageType('PlaceOrderResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLACEORDERRESPONSE,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.PlaceOrderResponse)
  })
_sym_db.RegisterMessage(PlaceOrderResponse)

AdRequest = _reflection.GeneratedProtocolMessageType('AdRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADREQUEST,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.AdRequest)
  })
_sym_db.RegisterMessage(AdRequest)

AdResponse = _reflection.GeneratedProtocolMessageType('AdResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADRESPONSE,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.AdResponse)
  })
_sym_db.RegisterMessage(AdResponse)

Ad = _reflection.GeneratedProtocolMessageType('Ad', (_message.Message,), {
  'DESCRIPTOR' : _AD,
  '__module__' : 'proto.hipstershop.demo_pb2'
  # @@protoc_insertion_point(class_scope:hipstershop.Ad)
  })
_sym_db.RegisterMessage(Ad)

_CARTSERVICE = DESCRIPTOR.services_by_name['CartService']
_RECOMMENDATIONSERVICE = DESCRIPTOR.services_by_name['RecommendationService']
_PRODUCTCATALOGSERVICE = DESCRIPTOR.services_by_name['ProductCatalogService']
_SHIPPINGSERVICE = DESCRIPTOR.services_by_name['ShippingService']
_CURRENCYSERVICE = DESCRIPTOR.services_by_name['CurrencyService']
_PAYMENTSERVICE = DESCRIPTOR.services_by_name['PaymentService']
_EMAILSERVICE = DESCRIPTOR.services_by_name['EmailService']
_CHECKOUTSERVICE = DESCRIPTOR.services_by_name['CheckoutService']
_ADSERVICE = DESCRIPTOR.services_by_name['AdService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/ease-lab/vSwarm-proto/proto/hipstershop'
  _CARTITEM._serialized_start=45
  _CARTITEM._serialized_end=93
  _ADDITEMREQUEST._serialized_start=95
  _ADDITEMREQUEST._serialized_end=165
  _EMPTYCARTREQUEST._serialized_start=167
  _EMPTYCARTREQUEST._serialized_end=202
  _GETCARTREQUEST._serialized_start=204
  _GETCARTREQUEST._serialized_end=237
  _CART._serialized_start=239
  _CART._serialized_end=300
  _EMPTY._serialized_start=302
  _EMPTY._serialized_end=309
  _LISTRECOMMENDATIONSREQUEST._serialized_start=311
  _LISTRECOMMENDATIONSREQUEST._serialized_end=377
  _LISTRECOMMENDATIONSRESPONSE._serialized_start=379
  _LISTRECOMMENDATIONSRESPONSE._serialized_end=429
  _PRODUCT._serialized_start=432
  _PRODUCT._serialized_end=564
  _LISTPRODUCTSRESPONSE._serialized_start=566
  _LISTPRODUCTSRESPONSE._serialized_end=628
  _GETPRODUCTREQUEST._serialized_start=630
  _GETPRODUCTREQUEST._serialized_end=661
  _SEARCHPRODUCTSREQUEST._serialized_start=663
  _SEARCHPRODUCTSREQUEST._serialized_end=701
  _SEARCHPRODUCTSRESPONSE._serialized_start=703
  _SEARCHPRODUCTSRESPONSE._serialized_end=766
  _GETQUOTEREQUEST._serialized_start=768
  _GETQUOTEREQUEST._serialized_end=862
  _GETQUOTERESPONSE._serialized_start=864
  _GETQUOTERESPONSE._serialized_end=920
  _SHIPORDERREQUEST._serialized_start=922
  _SHIPORDERREQUEST._serialized_end=1017
  _SHIPORDERRESPONSE._serialized_start=1019
  _SHIPORDERRESPONSE._serialized_end=1059
  _ADDRESS._serialized_start=1061
  _ADDRESS._serialized_end=1158
  _MONEY._serialized_start=1160
  _MONEY._serialized_end=1220
  _GETSUPPORTEDCURRENCIESRESPONSE._serialized_start=1222
  _GETSUPPORTEDCURRENCIESRESPONSE._serialized_end=1278
  _CURRENCYCONVERSIONREQUEST._serialized_start=1280
  _CURRENCYCONVERSIONREQUEST._serialized_end=1358
  _CREDITCARDINFO._serialized_start=1361
  _CREDITCARDINFO._serialized_end=1505
  _CHARGEREQUEST._serialized_start=1507
  _CHARGEREQUEST._serialized_end=1608
  _CHARGERESPONSE._serialized_start=1610
  _CHARGERESPONSE._serialized_end=1650
  _ORDERITEM._serialized_start=1652
  _ORDERITEM._serialized_end=1734
  _ORDERRESULT._serialized_start=1737
  _ORDERRESULT._serialized_end=1928
  _SENDORDERCONFIRMATIONREQUEST._serialized_start=1930
  _SENDORDERCONFIRMATIONREQUEST._serialized_end=2016
  _PLACEORDERREQUEST._serialized_start=2019
  _PLACEORDERREQUEST._serialized_end=2182
  _PLACEORDERRESPONSE._serialized_start=2184
  _PLACEORDERRESPONSE._serialized_end=2245
  _ADREQUEST._serialized_start=2247
  _ADREQUEST._serialized_end=2280
  _ADRESPONSE._serialized_start=2282
  _ADRESPONSE._serialized_end=2324
  _AD._serialized_start=2326
  _AD._serialized_end=2366
  _CARTSERVICE._serialized_start=2369
  _CARTSERVICE._serialized_end=2571
  _RECOMMENDATIONSERVICE._serialized_start=2574
  _RECOMMENDATIONSERVICE._serialized_end=2705
  _PRODUCTCATALOGSERVICE._serialized_start=2708
  _PRODUCTCATALOGSERVICE._serialized_end=2967
  _SHIPPINGSERVICE._serialized_start=2970
  _SHIPPINGSERVICE._serialized_end=3140
  _CURRENCYSERVICE._serialized_start=3143
  _CURRENCYSERVICE._serialized_end=3326
  _PAYMENTSERVICE._serialized_start=3328
  _PAYMENTSERVICE._serialized_end=3413
  _EMAILSERVICE._serialized_start=3415
  _EMAILSERVICE._serialized_end=3519
  _CHECKOUTSERVICE._serialized_start=3521
  _CHECKOUTSERVICE._serialized_end=3619
  _ADSERVICE._serialized_start=3621
  _ADSERVICE._serialized_end=3693
# @@protoc_insertion_point(module_scope)
