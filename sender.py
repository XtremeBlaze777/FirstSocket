# Tutorials used: https://realpython.com/python-sockets/ , https://docs.python.org/3/library/socket.html

import socket
import sys
import json

# constants
TCP = socket.SOCK_STREAM
UDP = socket.SOCK_DGRAM
INTERNET_SOCKET = socket.AF_INET

# resources for the socket
max_bytes = 1024
host_ip = "127.0.0.1" # localhost
host_port = 65432 # random port > 5000
address = (host_ip, host_port)
client_name = "The Client"


with socket.socket(family=INTERNET_SOCKET, type=TCP) as client:
    client.connect(address)

    num2 = 7 # dummy initialization of num2
    try:
        num2 = int(sys.argv[1])
    except (IndexError, ValueError):
        print("You must provide an integer between 1 and 100\nPlease rerun both the server and client")
        client.sendall(json.dumps({}).encode())
        exit(1)

    client_packet = {'name':client_name, 'data':num2}
    client.sendall(json.dumps(client_packet).encode()) # encode turns it into "bytes-like object"

    host_packet = json.loads(client.recv(max_bytes).decode())
    host_name = host_packet["name"]
    num1 = host_packet["data"]
    
    print(f"{host_name} has connected to {client_name}")
    print(f"Sum of Values: {num1+num2}")
