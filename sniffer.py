import socket
import argparse

from protocols.ethernet import EthParser
from dissector import Dissector

DEFAULT_IFACE = "eth0"

def parse_args():
    parser = argparse.ArgumentParser(description="a sniffer for Ethernet devices")
    parser.add_argument("-i", default=DEFAULT_IFACE, dest="interface")
    return parser.parse_args()

class Sniffer:
    MAX_PKT_SIZE = 4096
    def __init__(self, iface, dissector):
        self.iface = iface
        self._socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 768)
        self.dissector = dissector

    def start(self):
        self._socket.bind((self.iface, 0))
        while True:
            data = self._socket.recvmsg(self.MAX_PKT_SIZE)[0]
            self.dissector.dissect(data)

    def stop(self):
        self._socket.close()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()

def main():
    args = parse_args()
    parser = EthParser()
    dissector = Dissector(parser)

    sniffer = Sniffer(args.interface, dissector)

    with sniffer:
        pass

if __name__ == "__main__":
    main()