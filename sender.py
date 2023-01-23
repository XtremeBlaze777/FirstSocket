# Tutorials used: https://realpython.com/python-sockets/ , https://docs.python.org/3/library/socket.html

import socket

# constants
TCP = socket.SOCK_STREAM
UDP = socket.SOCK_DGRAM
INTERNET_SOCKET = socket.AF_INET

# resources for the socket
max_bytes = 1024
host_ip = "127.0.0.1" # localhost
host_port = 65432 # random port > 5000
ADDRESS = (host_ip, host_port)

with socket.socket(family=INTERNET_SOCKET, type=TCP) as client:
    client.connect(ADDRESS)
    client.sendall(b"Hello server!") # b refers to "bytes-like object," not string
    data = client.recv(max_bytes)

print(f"Received {data!r}")