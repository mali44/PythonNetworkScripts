import sys
import socket
import ipaddress
import subprocess


print('-' * 30)
print('UDP Port Tarayıcı')
print('Shows open ports 1-65535')
print('-' * 30)
ipAddress = input("IPv4 Address: ")
str(ipAddress)
print('-' * 30)
for i in range(1,65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    result = sock.connect_ex((ipAddress, i))
    if result == 0:
        print(f"Port {i} Open")
    else:
        print(f"port {i} closed ")
print('-' * 30)