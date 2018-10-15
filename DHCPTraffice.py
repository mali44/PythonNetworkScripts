import socket
import sys

import dpkt

f = open("dhcp.pcap")
pcap = dpkt.pcap.Reader(f)
for ts, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    udp = ip.data
    dhcp = dpkt.dhcp.DHCP(udp.data)
    print("Kaynak")
    print("{} -> {}".format(socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst)))
