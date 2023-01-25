# Tutorials used: https://realpython.com/python-sockets/ , https://docs.python.org/3/library/socket.html

import socket
import json

# constants
TCP = socket.SOCK_STREAM
UDP = socket.SOCK_DGRAM
INTERNET_SOCKET = socket.AF_INET

# resources for the socket
max_bytes = 1024
host_name = "The Server"
host_ip = "127.0.0.1" # localhost
host_port = 65432 # random port > 5000
address = (host_ip, host_port)
host_packet = {'name':host_name, 'data':7} # random integer between 1-100 sent back to client; b refers to "bytes-like object"

with socket.socket(family=INTERNET_SOCKET, type=TCP) as host:
    host.bind(address)
    host.listen()

    ''' @return client = the client socket
        @return client_ip = the IP address the client socket is bound to '''
    client, client_ip = host.accept()
    
    with client:

        # receive data from the client
        while True:
            client_packet = json.loads(client.recv(max_bytes).decode())
            if not client_packet:
                print("Did not receive an integer between 1 and 100; closing server")
                break
            client_name = client_packet["name"]
            num2 = client_packet["data"]
            if not (num2 >= 1 and num2 <= 100):
                print("You must provide an integer between 1 and 100\nPlease rerun both the server and client")
                break
            client.sendall(json.dumps(host_packet).encode())
            print(f"{host_name} has connected to {client_name}")
            break
