# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bot_builder.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x62ot_builder.proto\x12\x13\x62ot_builder.service\"(\n\x15GetStoryBlocksRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\x8b\x01\n\nStoryBlock\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x11\n\tparent_id\x18\x05 \x01(\t\x12\x31\n\x08\x63hildren\x18\x06 \x03(\x0b\x32\x1f.bot_builder.service.StoryBlock\"0\n\x16GetBotResponsesRequest\x12\x16\n\x0estory_block_id\x18\x02 \x01(\t\"N\n\x17GetBotResponsesResponse\x12\x33\n\tresponses\x18\x01 \x03(\x0b\x32 .bot_builder.service.BotResponse\"-\n\x0b\x42otResponse\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08variants\x18\x02 \x03(\t2\xe0\x01\n\x11\x42otBuilderService\x12]\n\x0eGetStoryBlocks\x12*.bot_builder.service.GetStoryBlocksRequest\x1a\x1f.bot_builder.service.StoryBlock\x12l\n\x0fGetBotResponses\x12+.bot_builder.service.GetBotResponsesRequest\x1a,.bot_builder.service.GetBotResponsesResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bot_builder_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETSTORYBLOCKSREQUEST']._serialized_start=42
  _globals['_GETSTORYBLOCKSREQUEST']._serialized_end=82
  _globals['_STORYBLOCK']._serialized_start=85
  _globals['_STORYBLOCK']._serialized_end=224
  _globals['_GETBOTRESPONSESREQUEST']._serialized_start=226
  _globals['_GETBOTRESPONSESREQUEST']._serialized_end=274
  _globals['_GETBOTRESPONSESRESPONSE']._serialized_start=276
  _globals['_GETBOTRESPONSESRESPONSE']._serialized_end=354
  _globals['_BOTRESPONSE']._serialized_start=356
  _globals['_BOTRESPONSE']._serialized_end=401
  _globals['_BOTBUILDERSERVICE']._serialized_start=404
  _globals['_BOTBUILDERSERVICE']._serialized_end=628
# @@protoc_insertion_point(module_scope)