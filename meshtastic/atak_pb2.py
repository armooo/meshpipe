# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/atak.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15meshtastic/atak.proto\x12\nmeshtastic\"\xe6\x01\n\tTAKPacket\x12\x15\n\ris_compressed\x18\x01 \x01(\x08\x12$\n\x07\x63ontact\x18\x02 \x01(\x0b\x32\x13.meshtastic.Contact\x12 \n\x05group\x18\x03 \x01(\x0b\x32\x11.meshtastic.Group\x12\"\n\x06status\x18\x04 \x01(\x0b\x32\x12.meshtastic.Status\x12\x1e\n\x03pli\x18\x05 \x01(\x0b\x32\x0f.meshtastic.PLIH\x00\x12#\n\x04\x63hat\x18\x06 \x01(\x0b\x32\x13.meshtastic.GeoChatH\x00\x42\x11\n\x0fpayload_variant\"2\n\x07GeoChat\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x02to\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x05\n\x03_to\"M\n\x05Group\x12$\n\x04role\x18\x01 \x01(\x0e\x32\x16.meshtastic.MemberRole\x12\x1e\n\x04team\x18\x02 \x01(\x0e\x32\x10.meshtastic.Team\"\x19\n\x06Status\x12\x0f\n\x07\x62\x61ttery\x18\x01 \x01(\r\"4\n\x07\x43ontact\x12\x10\n\x08\x63\x61llsign\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65vice_callsign\x18\x02 \x01(\t\"_\n\x03PLI\x12\x12\n\nlatitude_i\x18\x01 \x01(\x0f\x12\x13\n\x0blongitude_i\x18\x02 \x01(\x0f\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x05\x12\r\n\x05speed\x18\x04 \x01(\r\x12\x0e\n\x06\x63ourse\x18\x05 \x01(\r*\xc0\x01\n\x04Team\x12\x14\n\x10Unspecifed_Color\x10\x00\x12\t\n\x05White\x10\x01\x12\n\n\x06Yellow\x10\x02\x12\n\n\x06Orange\x10\x03\x12\x0b\n\x07Magenta\x10\x04\x12\x07\n\x03Red\x10\x05\x12\n\n\x06Maroon\x10\x06\x12\n\n\x06Purple\x10\x07\x12\r\n\tDark_Blue\x10\x08\x12\x08\n\x04\x42lue\x10\t\x12\x08\n\x04\x43yan\x10\n\x12\x08\n\x04Teal\x10\x0b\x12\t\n\x05Green\x10\x0c\x12\x0e\n\nDark_Green\x10\r\x12\t\n\x05\x42rown\x10\x0e*\x7f\n\nMemberRole\x12\x0e\n\nUnspecifed\x10\x00\x12\x0e\n\nTeamMember\x10\x01\x12\x0c\n\x08TeamLead\x10\x02\x12\x06\n\x02HQ\x10\x03\x12\n\n\x06Sniper\x10\x04\x12\t\n\x05Medic\x10\x05\x12\x13\n\x0f\x46orwardObserver\x10\x06\x12\x07\n\x03RTO\x10\x07\x12\x06\n\x02K9\x10\x08\x42_\n\x13\x63om.geeksville.meshB\nATAKProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.atak_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\nATAKProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _TEAM._serialized_start=580
  _TEAM._serialized_end=772
  _MEMBERROLE._serialized_start=774
  _MEMBERROLE._serialized_end=901
  _TAKPACKET._serialized_start=38
  _TAKPACKET._serialized_end=268
  _GEOCHAT._serialized_start=270
  _GEOCHAT._serialized_end=320
  _GROUP._serialized_start=322
  _GROUP._serialized_end=399
  _STATUS._serialized_start=401
  _STATUS._serialized_end=426
  _CONTACT._serialized_start=428
  _CONTACT._serialized_end=480
  _PLI._serialized_start=482
  _PLI._serialized_end=577
# @@protoc_insertion_point(module_scope)
