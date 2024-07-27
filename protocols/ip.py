from construct import *
from dataclasses import dataclass

from core.base_parser import BaseParser
from core.base_packet import BasePacket

from protocols.icmp import ICMPParser

IPPROTO_ICMP = 1

IP_HEADER_FIELDS = {
    "version": Nibble,
    "header_length": Nibble,
    "diff_services": Octet,
    "tot_len": Bytewise(Short),
    "ident": Bytewise(Short),
    "flags": BitsInteger(3),
    "fragment_offset": BitsInteger(13),
    "ttl": Octet,
    "proto": Octet,
    "checksum": Bytewise(Short),
    "src": Bytewise(Int32ub),
    "dst": Bytewise(Int32ub)
}

@dataclass
class IPPacket(BasePacket):
    version: int
    header_length: int
    diff_services: int
    tot_len: int
    ident: int
    flags: int
    fragment_offset: int
    ttl: int
    proto: int
    checksum: int
    src: int
    dst: int

class IPParser(BaseParser):
    HEADER_STRUCT = BitStruct(
        **IP_HEADER_FIELDS
    )
    PACKET_TYPE = IPPacket
    NEXT_PARSER = {IPPROTO_ICMP: ICMPParser}
    NEXT_PARSER_FIELD_NAME = "proto"