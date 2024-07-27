## Sniffer
This project is my makeshift copy of wireshark.
It opens a raw socket on an Ethernet device and sniffs packets on it.

## Supported protocols
The sniffer can parse Ethernet, ARP, IP and ICMP packets.
Each protocol's specification is under the `protocols` directory.

However, this sniffer has a generic infrastructure (see the `core` directory), and can be easily expanded to support more protocols.

## Features to add in the future
1. Make a `Field` class that will enable me to print each field in each protocol individually.
for example, an IP address should be printed like this `%d.%d.%d.%d`, while a MAC address should look like this: `%d:%d:%d:%d:%d:%d`. This will also enable me to map values to meaningful strings (for example, I would rather print `IPv4` instead of `0x0800` when parsing the `ethertype` field of an Ethernet header).
2. Have a `-w` option that will save the packets to a `.pcap` file.
For this I would love to have a generic output class that `Sniffer` uses instead of my current `Dissector`...
3. Support more protocols (TCP, UDP, HTTP, DNS, DHCP, ...)
4. Have a code generation infrastructure that can generate the `*Parser` and `*Packet` classes for a new protocol. This is possible since all files in the `protocols` directory have the same overall structure.
5. Exit gracefully on `Ctrl+C`
6. Have the sniffing in a separate thread, so that `with Sniffer()` will have an actual meaning