# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trainer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rtrainer.proto\x12\nou_pokemon\x1a\x1bgoogle/protobuf/empty.proto\"\x1c\n\x08\x46\x65\x65\x64\x62\x61\x63k\x12\x10\n\x08\x66\x65\x65\x64\x62\x61\x63k\x18\x01 \x01(\t\"*\n\x0b\x42oardConfig\x12\x0b\n\x03row\x18\x01 \x01(\x05\x12\x0e\n\x06\x63olumn\x18\x02 \x01(\x05\"\x1c\n\x0cMoveDecision\x12\x0c\n\x04move\x18\x01 \x01(\t\"4\n\x0bPokemonList\x12%\n\x04name\x18\x01 \x03(\x0b\x32\x17.ou_pokemon.PokemonName\"\x1b\n\x0bPokemonName\x12\x0c\n\x04name\x18\x01 \x01(\t\"6\n\x08MoveList\x12*\n\x08movelist\x18\x01 \x03(\x0b\x32\x18.ou_pokemon.MoveDecision2\xbc\x02\n\x0ePokemonTrainer\x12\x37\n\x07\x43\x61pture\x12\x14.ou_pokemon.Feedback\x1a\x14.ou_pokemon.Feedback\"\x00\x12\x41\n\nCheckboard\x12\x17.ou_pokemon.BoardConfig\x1a\x18.ou_pokemon.MoveDecision\"\x00\x12\x38\n\x04Move\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12<\n\x07Pokedex\x12\x16.google.protobuf.Empty\x1a\x17.ou_pokemon.PokemonList\"\x00\x12\x36\n\x04Path\x12\x16.google.protobuf.Empty\x1a\x14.ou_pokemon.MoveList\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'trainer_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FEEDBACK._serialized_start=58
  _FEEDBACK._serialized_end=86
  _BOARDCONFIG._serialized_start=88
  _BOARDCONFIG._serialized_end=130
  _MOVEDECISION._serialized_start=132
  _MOVEDECISION._serialized_end=160
  _POKEMONLIST._serialized_start=162
  _POKEMONLIST._serialized_end=214
  _POKEMONNAME._serialized_start=216
  _POKEMONNAME._serialized_end=243
  _MOVELIST._serialized_start=245
  _MOVELIST._serialized_end=299
  _POKEMONTRAINER._serialized_start=302
  _POKEMONTRAINER._serialized_end=618
# @@protoc_insertion_point(module_scope)