# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pokemon.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rpokemon.proto\x12\nou_pokemon\"\x1c\n\x0bPokemonName\x12\r\n\x05pname\x18\x01 \x01(\t\"\x18\n\x06Player\x12\x0e\n\x06player\x18\x01 \x01(\t\";\n\x08\x46\x65\x65\x64\x62\x61\x63k\x12\x0e\n\x06rowNum\x18\x01 \x01(\x05\x12\x11\n\tcolumnNum\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\"*\n\x0b\x42oardConfig\x12\x0b\n\x03row\x18\x01 \x01(\x05\x12\x0e\n\x06\x63olumn\x18\x02 \x01(\x05\x32\xc5\x01\n\rOUPokemanGame\x12>\n\x08\x43\x61ptured\x12\x17.ou_pokemon.PokemonName\x1a\x17.ou_pokemon.PokemonName\"\x00\x12\x37\n\x05Moves\x12\x12.ou_pokemon.Player\x1a\x14.ou_pokemon.Feedback\"\x00(\x01\x30\x01\x12;\n\x05\x42oard\x12\x17.ou_pokemon.BoardConfig\x1a\x17.ou_pokemon.BoardConfig\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pokemon_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POKEMONNAME._serialized_start=29
  _POKEMONNAME._serialized_end=57
  _PLAYER._serialized_start=59
  _PLAYER._serialized_end=83
  _FEEDBACK._serialized_start=85
  _FEEDBACK._serialized_end=144
  _BOARDCONFIG._serialized_start=146
  _BOARDCONFIG._serialized_end=188
  _OUPOKEMANGAME._serialized_start=191
  _OUPOKEMANGAME._serialized_end=388
# @@protoc_insertion_point(module_scope)
