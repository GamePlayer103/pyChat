import socket
import threading
from log import Logs

SERVER_ADDRESS= '127.0.0.1'
SERVER_PORT = 1234

logs = Logs('log.txt')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_ADDRESS, SERVER_PORT))
server.listen()
logs.log(f'Server is listening on {str(SERVER_ADDRESS)}, {str(SERVER_PORT)}')

clients = []

def broadcast_message(message):
    '''
    Broadcasts message to all possbile clients
    '''
    for client in clients:
        client.send(message.encode())

def listen_for_messages(client):
    '''
    Listen for messages from client and removes the client from clients list when disconnected
    '''
    while True:
        message = client.recv(1024).decode()
        
        if message:
            broadcast_message(f'<{str(client.getpeername())}>: {message}')
        else:
            clients.remove(client)
            logs.log(f'{str(client.getpeername())} has disconnected from the server')
            broadcast_message(f'{str(client.getpeername())} has left the chat!')
            break

while True:
    client, address = server.accept()
    logs.log(f'Client is connected on {str(address)}')

    clients.append(client)

    thread = threading.Thread(target=listen_for_messages, args=(client,))
    thread.deamon = True
    thread.start()

    broadcast_message(f'{str(address)} has joined the chat!')
