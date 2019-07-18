
import commands
import socket
import threading
import sys
def startServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 10_000))
    return server.listen(5)
    '''
    while True:
        client_sock, address = server.accept()
        print
        'Accepted connection from {}:{}'.format(address[0], address[1])
        client_handler = threading.Thread(
            target=handle_client_connection,
            args=(client_sock,)
        )
        client_handler.start()
        '''

def connectTo(IP):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (IP, 10_000)
    return client.connect(server_address)
    """
    while True:
        client.send(input("Type what to send : ").encode())
        response = client.recv(4096)
        print("Received : " + response.decode())
    """

def handle_client_connection(client_socket):
    while True:
        request = client_socket.recv(4096)
        print('Received {}'.format(request.decode()))
        client_socket.send('ACK!'.encode())