from construct import *
from dataclasses import dataclass

from core.base_parser import BaseParser
from core.base_packet import BasePacket

from protocols.ip import IPParser
from protocols.arp import ARPParser


ETHERTYPE_IP = 0x800
ETHERTYPE_ARP = 0x806

MAC_ADDRESS_SIZE = 6

ETHERNET_HEADER_FIELDS = {
    "dst" : Bytes(MAC_ADDRESS_SIZE),
    "src" : Bytes(MAC_ADDRESS_SIZE),
    "type": Short,
}

@dataclass
class EthPacket(BasePacket):
    dst: bytes
    src: bytes
    type: int

class EthParser(BaseParser):
    HEADER_STRUCT = Struct(
        **ETHERNET_HEADER_FIELDS
    )

    NEXT_PARSER = {ETHERTYPE_IP: IPParser, ETHERTYPE_ARP: ARPParser}
    PACKET_TYPE = EthPacket
    NEXT_PARSER_FIELD_NAME = "type"
        