from construct import *
from dataclasses import dataclass

from core.base_parser import BaseParser
from core.base_packet import BasePacket


HW_ADDR_SIZE = 6
PROTO_ADDR_SIZE = 4

ARP_HEADER_FIELDS = {
    "hw_type": Short,
    "proto_type": Short,
    "hw_size": Byte,
    "proto_size": Byte,
    "opcode": Byte,
    "hw_src": Bytes(HW_ADDR_SIZE),
    "proto_src": Bytes(PROTO_ADDR_SIZE),
    "hw_dst": Bytes(HW_ADDR_SIZE),
    "proto_dst": Bytes(PROTO_ADDR_SIZE),
}

@dataclass
class NamedObject:
    name: str

@dataclass
class ARPPacket(BasePacket):
    hw_type: int
    proto_type: int
    hw_size: int
    proto_size: int
    opcode: int
    hw_src: bytes
    proto_src: bytes
    hw_dst: bytes
    proto_dst: bytes

class ARPParser(BaseParser):
    HEADER_STRUCT = Struct(
        **ARP_HEADER_FIELDS
    )
    PACKET_TYPE = ARPPacket
    NEXT_PARSER = {}
    NEXT_PARSER_FIELD_NAME = ""