import socket
import threading

SERVER_ADDRESS= '127.0.0.1'
SERVER_PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_ADDRESS, SERVER_PORT))
server.listen()
print(f'Server is listening on {str(SERVER_ADDRESS)}, {str(SERVER_PORT)}')

while True:
    client, address = server.accept()
    print(f'Client is connected on {str(address)}')
