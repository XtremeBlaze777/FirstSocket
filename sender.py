# Tutorials used: https://realpython.com/python-sockets/ , https://docs.python.org/3/library/socket.html

import socket
import sys

# constants
TCP = socket.SOCK_STREAM
UDP = socket.SOCK_DGRAM
INTERNET_SOCKET = socket.AF_INET

# resources for the socket
max_bytes = 1024
host_ip = "127.0.0.1" # localhost
host_port = 65432 # random port > 5000
ADDRESS = (host_ip, host_port)

exit_flag = False

with socket.socket(family=INTERNET_SOCKET, type=TCP) as client:
    client.connect(ADDRESS)

    try:
        num2 = int(sys.argv[1])
        client.sendall(str(num2).encode("ascii")) # encode turns it into "bytes-like object"
        num1 = int(client.recv(max_bytes).decode())
    except (IndexError, ValueError):
        print("You must provide an integer between 1 and 100\nPlease rerun both the server and client")
        client.sendall(b'-1')
        exit_flag = True
        
if exit_flag:
    exit(1)
else:
    print(f"Sum of Values: {num1+num2}")