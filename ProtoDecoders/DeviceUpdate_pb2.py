# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ProtoDecoders/DeviceUpdate.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ProtoDecoders import Common_pb2 as ProtoDecoders_dot_Common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n ProtoDecoders/DeviceUpdate.proto\x1a\x1aProtoDecoders/Common.proto\"6\n\x0b\x44\x65vicesList\x12\'\n\x0e\x64\x65viceMetadata\x18\x02 \x03(\x0b\x32\x0f.DeviceMetadata\"R\n\x12\x44\x65vicesListRequest\x12<\n\x18\x64\x65viceListRequestPayload\x18\x01 \x01(\x0b\x32\x1a.DevicesListRequestPayload\"B\n\x19\x44\x65vicesListRequestPayload\x12\x19\n\x04type\x18\x01 \x01(\x0e\x32\x0b.DeviceType\x12\n\n\x02id\x18\x03 \x01(\t\"\x96\x01\n\x14\x45xecuteActionRequest\x12\"\n\x05scope\x18\x01 \x01(\x0b\x32\x13.ExecuteActionScope\x12\"\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\x12.ExecuteActionType\x12\x36\n\x0frequestMetadata\x18\x03 \x01(\x0b\x32\x1d.ExecuteActionRequestMetadata\"\xaf\x01\n\x1c\x45xecuteActionRequestMetadata\x12\x19\n\x04type\x18\x01 \x01(\x0e\x32\x0b.DeviceType\x12\x13\n\x0brequestUuid\x18\x02 \x01(\t\x12\x15\n\rfmdClientUuid\x18\x03 \x01(\t\x12\x37\n\x11gcmRegistrationId\x18\x04 \x01(\x0b\x32\x1c.GcmCloudMessagingIdProtobuf\x12\x0f\n\x07unknown\x18\x06 \x01(\x08\")\n\x1bGcmCloudMessagingIdProtobuf\x12\n\n\x02id\x18\x01 \x01(\t\"\xa4\x01\n\x11\x45xecuteActionType\x12\x36\n\rlocateTracker\x18\x1e \x01(\x0b\x32\x1f.ExecuteActionLocateTrackerType\x12+\n\nstartSound\x18\x1f \x01(\x0b\x32\x17.ExecuteActionSoundType\x12*\n\tstopSound\x18  \x01(\x0b\x32\x17.ExecuteActionSoundType\"n\n\x1e\x45xecuteActionLocateTrackerType\x12\x1d\n\x0e\x61\x63tivationDate\x18\x02 \x01(\x0b\x32\x05.Time\x12-\n\x0f\x63ontributorType\x18\x03 \x01(\x0e\x32\x14.SpotContributorType\"=\n\x16\x45xecuteActionSoundType\x12#\n\tcomponent\x18\x01 \x01(\x0e\x32\x10.DeviceComponent\"_\n\x12\x45xecuteActionScope\x12\x19\n\x04type\x18\x02 \x01(\x0e\x32\x0b.DeviceType\x12.\n\x06\x64\x65vice\x18\x03 \x01(\x0b\x32\x1e.ExecuteActionDeviceIdentifier\">\n\x1d\x45xecuteActionDeviceIdentifier\x12\x1d\n\tcanonicId\x18\x01 \x01(\x0b\x32\n.CanonicId\"\x96\x01\n\x0c\x44\x65viceUpdate\x12\x32\n\x0b\x66\x63mMetadata\x18\x01 \x01(\x0b\x32\x1d.ExecuteActionRequestMetadata\x12\'\n\x0e\x64\x65viceMetadata\x18\x03 \x01(\x0b\x32\x0f.DeviceMetadata\x12)\n\x0frequestMetadata\x18\x02 \x01(\x0b\x32\x10.RequestMetadata\"\xbd\x01\n\x0e\x44\x65viceMetadata\x12\x36\n\x15identifierInformation\x18\x01 \x01(\x0b\x32\x17.IdentitfierInformation\x12\'\n\x0binformation\x18\x04 \x01(\x0b\x32\x12.DeviceInformation\x12\x1d\n\x15userDefinedDeviceName\x18\x05 \x01(\t\x12+\n\x10imageInformation\x18\x06 \x01(\x0b\x32\x11.ImageInformation\"$\n\x10ImageInformation\x12\x10\n\x08imageUrl\x18\x01 \x01(\t\"9\n\x16IdentitfierInformation\x12\x1f\n\ncanonicIds\x18\x03 \x01(\x0b\x32\x0b.CanonicIds\"+\n\nCanonicIds\x12\x1d\n\tcanonicId\x18\x01 \x03(\x0b\x32\n.CanonicId\"\x17\n\tCanonicId\x12\n\n\x02id\x18\x01 \x01(\t\"\xb6\x01\n\x11\x44\x65viceInformation\x12?\n\x1a\x65phemeralDeviceInformation\x18\x01 \x01(\x0b\x32\x1b.EphemeralDeviceInformation\x12\x31\n\x13locationInformation\x18\x02 \x01(\x0b\x32\x14.LocationInformation\x12-\n\x11\x61\x63\x63\x65ssInformation\x18\x03 \x03(\x0b\x32\x12.AccessInformation\"<\n\x15\x44\x65viceTypeInformation\x12#\n\ndeviceType\x18\x02 \x01(\x0e\x32\x0f.SpotDeviceType\"\x9f\x01\n\x1a\x45phemeralDeviceInformation\x12\x35\n\x15\x64\x65viceTypeInformation\x18\x02 \x01(\x0b\x32\x16.DeviceTypeInformation\x12%\n\rencryptedKeys\x18\x13 \x01(\x0b\x32\x0e.EncryptedKeys\x12\x14\n\x0cmanufacturer\x18\x14 \x01(\t\x12\r\n\x05model\x18\" \x01(\t\"\xab\x01\n\rEncryptedKeys\x12\x1c\n\x14\x65ncryptedIdentityKey\x18\x01 \x01(\x0c\x12\x12\n\nkeyVersion\x18\x03 \x01(\x05\x12\x1b\n\x13\x65ncryptedAccountKey\x18\x04 \x01(\x0c\x12\x1b\n\x0ckeyTimestamp\x18\x08 \x01(\x0b\x32\x05.Time\x12.\n&encryptedSha256AccountKeyPublicAddress\x18\x0b \x01(\x0c\"F\n\x13LocationInformation\x12/\n\x07reports\x18\x03 \x01(\x0b\x32\x1e.LocationsAndTimestampsWrapper\"n\n\x1dLocationsAndTimestampsWrapper\x12M\n!recentLocationAndNetworkLocations\x18\x04 \x01(\x0b\x32\".RecentLocationAndNetworkLocations\"\x95\x02\n!RecentLocationAndNetworkLocations\x12\x38\n\x0erecentLocation\x18\x01 \x01(\x0b\x32 .LocationStatusAndRotationOffset\x12&\n\x17recentLocationTimestamp\x18\x02 \x01(\x0b\x32\x05.Time\x12:\n\x10networkLocations\x18\x05 \x03(\x0b\x32 .LocationStatusAndRotationOffset\x12(\n\x19networkLocationTimestamps\x18\x06 \x03(\x0b\x32\x05.Time\x12(\n minLocationsNeededForAggregation\x18\t \x01(\r\"{\n\x1fLocationStatusAndRotationOffset\x12?\n\x1blocationAndDeviceTimeOffset\x18\n \x01(\x0b\x32\x1a.LocationAndRotationOffset\x12\x17\n\x06status\x18\x0b \x01(\x0e\x32\x07.Status\"[\n\x11\x41\x63\x63\x65ssInformation\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x11\n\thasAccess\x18\x02 \x01(\x08\x12\x0f\n\x07isOwner\x18\x03 \x01(\x08\x12\x13\n\x0bthisAccount\x18\x04 \x01(\x08\".\n\x0fRequestMetadata\x12\x1b\n\x0cresponseTime\x18\x01 \x01(\x0b\x32\x05.Time*\xa5\x01\n\nDeviceType\x12\x17\n\x13UNKNOWN_DEVICE_TYPE\x10\x00\x12\x12\n\x0e\x41NDROID_DEVICE\x10\x01\x12\x0f\n\x0bSPOT_DEVICE\x10\x02\x12\x14\n\x10TEST_DEVICE_TYPE\x10\x03\x12\x0f\n\x0b\x41UTO_DEVICE\x10\x04\x12\x13\n\x0f\x46\x41STPAIR_DEVICE\x10\x05\x12\x1d\n\x19SUPERVISED_ANDROID_DEVICE\x10\x07*\xa6\x01\n\x13SpotContributorType\x12\x19\n\x15\x46MDN_DISABLED_DEFAULT\x10\x00\x12!\n\x1d\x46MDN_CONTRIBUTOR_HIGH_TRAFFIC\x10\x03\x12\"\n\x1e\x46MDN_CONTRIBUTOR_ALL_LOCATIONS\x10\x04\x12\x15\n\x11\x46MDN_HIGH_TRAFFIC\x10\x01\x12\x16\n\x12\x46MDN_ALL_LOCATIONS\x10\x02*\x85\x01\n\x0f\x44\x65viceComponent\x12 \n\x1c\x44\x45VICE_COMPONENT_UNSPECIFIED\x10\x00\x12\x1a\n\x16\x44\x45VICE_COMPONENT_RIGHT\x10\x01\x12\x19\n\x15\x44\x45VICE_COMPONENT_LEFT\x10\x02\x12\x19\n\x15\x44\x45VICE_COMPONENT_CASE\x10\x03*H\n\x06Status\x12\x0c\n\x08SEMANTIC\x10\x00\x12\x0e\n\nLAST_KNOWN\x10\x01\x12\x10\n\x0c\x43ROWDSOURCED\x10\x02\x12\x0e\n\nAGGREGATED\x10\x03*\x82\x05\n\x0eSpotDeviceType\x12\x17\n\x13\x44\x45VICE_TYPE_UNKNOWN\x10\x00\x12\x16\n\x12\x44\x45VICE_TYPE_BEACON\x10\x01\x12\x1a\n\x16\x44\x45VICE_TYPE_HEADPHONES\x10\x02\x12\x14\n\x10\x44\x45VICE_TYPE_KEYS\x10\x03\x12\x15\n\x11\x44\x45VICE_TYPE_WATCH\x10\x04\x12\x16\n\x12\x44\x45VICE_TYPE_WALLET\x10\x05\x12\x13\n\x0f\x44\x45VICE_TYPE_BAG\x10\x07\x12\x16\n\x12\x44\x45VICE_TYPE_LAPTOP\x10\x08\x12\x13\n\x0f\x44\x45VICE_TYPE_CAR\x10\t\x12\x1e\n\x1a\x44\x45VICE_TYPE_REMOTE_CONTROL\x10\n\x12\x15\n\x11\x44\x45VICE_TYPE_BADGE\x10\x0b\x12\x14\n\x10\x44\x45VICE_TYPE_BIKE\x10\x0c\x12\x16\n\x12\x44\x45VICE_TYPE_CAMERA\x10\r\x12\x13\n\x0f\x44\x45VICE_TYPE_CAT\x10\x0e\x12\x17\n\x13\x44\x45VICE_TYPE_CHARGER\x10\x0f\x12\x18\n\x14\x44\x45VICE_TYPE_CLOTHING\x10\x10\x12\x13\n\x0f\x44\x45VICE_TYPE_DOG\x10\x11\x12\x18\n\x14\x44\x45VICE_TYPE_NOTEBOOK\x10\x12\x12\x18\n\x14\x44\x45VICE_TYPE_PASSPORT\x10\x13\x12\x15\n\x11\x44\x45VICE_TYPE_PHONE\x10\x14\x12\x17\n\x13\x44\x45VICE_TYPE_SPEAKER\x10\x15\x12\x16\n\x12\x44\x45VICE_TYPE_TABLET\x10\x16\x12\x13\n\x0f\x44\x45VICE_TYPE_TOY\x10\x17\x12\x18\n\x14\x44\x45VICE_TYPE_UMBRELLA\x10\x18\x12\x16\n\x12\x44\x45VICE_TYPE_STYLUS\x10\x19\x12\x17\n\x13\x44\x45VICE_TYPE_EARBUDS\x10\x1a\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ProtoDecoders.DeviceUpdate_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DEVICETYPE']._serialized_start=2975
  _globals['_DEVICETYPE']._serialized_end=3140
  _globals['_SPOTCONTRIBUTORTYPE']._serialized_start=3143
  _globals['_SPOTCONTRIBUTORTYPE']._serialized_end=3309
  _globals['_DEVICECOMPONENT']._serialized_start=3312
  _globals['_DEVICECOMPONENT']._serialized_end=3445
  _globals['_STATUS']._serialized_start=3447
  _globals['_STATUS']._serialized_end=3519
  _globals['_SPOTDEVICETYPE']._serialized_start=3522
  _globals['_SPOTDEVICETYPE']._serialized_end=4164
  _globals['_DEVICESLIST']._serialized_start=64
  _globals['_DEVICESLIST']._serialized_end=118
  _globals['_DEVICESLISTREQUEST']._serialized_start=120
  _globals['_DEVICESLISTREQUEST']._serialized_end=202
  _globals['_DEVICESLISTREQUESTPAYLOAD']._serialized_start=204
  _globals['_DEVICESLISTREQUESTPAYLOAD']._serialized_end=270
  _globals['_EXECUTEACTIONREQUEST']._serialized_start=273
  _globals['_EXECUTEACTIONREQUEST']._serialized_end=423
  _globals['_EXECUTEACTIONREQUESTMETADATA']._serialized_start=426
  _globals['_EXECUTEACTIONREQUESTMETADATA']._serialized_end=601
  _globals['_GCMCLOUDMESSAGINGIDPROTOBUF']._serialized_start=603
  _globals['_GCMCLOUDMESSAGINGIDPROTOBUF']._serialized_end=644
  _globals['_EXECUTEACTIONTYPE']._serialized_start=647
  _globals['_EXECUTEACTIONTYPE']._serialized_end=811
  _globals['_EXECUTEACTIONLOCATETRACKERTYPE']._serialized_start=813
  _globals['_EXECUTEACTIONLOCATETRACKERTYPE']._serialized_end=923
  _globals['_EXECUTEACTIONSOUNDTYPE']._serialized_start=925
  _globals['_EXECUTEACTIONSOUNDTYPE']._serialized_end=986
  _globals['_EXECUTEACTIONSCOPE']._serialized_start=988
  _globals['_EXECUTEACTIONSCOPE']._serialized_end=1083
  _globals['_EXECUTEACTIONDEVICEIDENTIFIER']._serialized_start=1085
  _globals['_EXECUTEACTIONDEVICEIDENTIFIER']._serialized_end=1147
  _globals['_DEVICEUPDATE']._serialized_start=1150
  _globals['_DEVICEUPDATE']._serialized_end=1300
  _globals['_DEVICEMETADATA']._serialized_start=1303
  _globals['_DEVICEMETADATA']._serialized_end=1492
  _globals['_IMAGEINFORMATION']._serialized_start=1494
  _globals['_IMAGEINFORMATION']._serialized_end=1530
  _globals['_IDENTITFIERINFORMATION']._serialized_start=1532
  _globals['_IDENTITFIERINFORMATION']._serialized_end=1589
  _globals['_CANONICIDS']._serialized_start=1591
  _globals['_CANONICIDS']._serialized_end=1634
  _globals['_CANONICID']._serialized_start=1636
  _globals['_CANONICID']._serialized_end=1659
  _globals['_DEVICEINFORMATION']._serialized_start=1662
  _globals['_DEVICEINFORMATION']._serialized_end=1844
  _globals['_DEVICETYPEINFORMATION']._serialized_start=1846
  _globals['_DEVICETYPEINFORMATION']._serialized_end=1906
  _globals['_EPHEMERALDEVICEINFORMATION']._serialized_start=1909
  _globals['_EPHEMERALDEVICEINFORMATION']._serialized_end=2068
  _globals['_ENCRYPTEDKEYS']._serialized_start=2071
  _globals['_ENCRYPTEDKEYS']._serialized_end=2242
  _globals['_LOCATIONINFORMATION']._serialized_start=2244
  _globals['_LOCATIONINFORMATION']._serialized_end=2314
  _globals['_LOCATIONSANDTIMESTAMPSWRAPPER']._serialized_start=2316
  _globals['_LOCATIONSANDTIMESTAMPSWRAPPER']._serialized_end=2426
  _globals['_RECENTLOCATIONANDNETWORKLOCATIONS']._serialized_start=2429
  _globals['_RECENTLOCATIONANDNETWORKLOCATIONS']._serialized_end=2706
  _globals['_LOCATIONSTATUSANDROTATIONOFFSET']._serialized_start=2708
  _globals['_LOCATIONSTATUSANDROTATIONOFFSET']._serialized_end=2831
  _globals['_ACCESSINFORMATION']._serialized_start=2833
  _globals['_ACCESSINFORMATION']._serialized_end=2924
  _globals['_REQUESTMETADATA']._serialized_start=2926
  _globals['_REQUESTMETADATA']._serialized_end=2972
# @@protoc_insertion_point(module_scope)
