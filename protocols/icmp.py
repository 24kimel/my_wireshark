from construct import *
from dataclasses import dataclass

from core.base_parser import BaseParser
from core.base_packet import BasePacket

ICMP_HEADER_FIELDS = {
    "type": Byte,
    "code": Byte,
    "checksum": Short,
    "identifier": Short,
    "sequence": Short
}

@dataclass
class ICMPPacket(BasePacket):
    type: int
    code: int
    checksum: int
    identifier: int
    sequence: int

class ICMPParser(BaseParser):
    HEADER_STRUCT = Struct(
        **ICMP_HEADER_FIELDS
    )
    PACKET_TYPE = ICMPPacket
    NEXT_PARSER = {}
    NEXT_PARSER_FIELD_NAME = ""