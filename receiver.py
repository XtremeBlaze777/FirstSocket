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

with socket.socket(family=INTERNET_SOCKET, type=TCP) as host:
    host.bind(ADDRESS)
    host.listen()

    ''' @return client = the client socket
        @return client_ip = the IP address the client socket is bound to '''
    client, client_ip = host.accept()
    
    with client:
        print(f"The server has connected to a client")

        # receive data from the client
        while True:
            data = client.recv(max_bytes)
            if not data:
                break
            client.sendall(data)
