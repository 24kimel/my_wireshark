class Dissector:
    def __init__(self, parser):
        self.parser = parser

    def dissect(self, data):
        parser = self.parser
        while True:
            packet = parser.parse(data)
            print(str(packet))
            data = data[parser.HEADER_STRUCT.sizeof():]
            next_parser_class = parser.get_next_parser_class(packet)
            if next_parser_class is None:
                print(f"##### payload #####\n{data}\n")
                return
            parser = next_parser_class()