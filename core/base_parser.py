
class BaseParser:
    def _get_container_from_bytes(self, data):
        return self.HEADER_STRUCT.parse(data)

    def _get_packet_from_container(self, container):

        # got this field from construct...
        container.pop("_io")

        return self.PACKET_TYPE(**dict(container))

    def parse(self, data):
        container = self._get_container_from_bytes(data)
        packet = self._get_packet_from_container(container)
        return packet

    def get_next_parser_class(self, packet):
        if hasattr(packet, self.NEXT_PARSER_FIELD_NAME):
            protocol_identifier = getattr(packet, self.NEXT_PARSER_FIELD_NAME)
            if protocol_identifier in self.NEXT_PARSER:
                return self.NEXT_PARSER[getattr(packet, self.NEXT_PARSER_FIELD_NAME)]

