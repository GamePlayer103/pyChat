import socket
import threading
import sys

if(len(sys.argv) != 3):
    print('Correct usage: client.py <server_ip adress> <server_port>')
    exit()

server_ip = str(sys.argv[1])
server_port = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(5)
print('Connecting to the server...')

try:
    client.connect((server_ip, server_port))
except socket.error as error:
    print('Connection error: ' + str(error))
    exit()

print('Connected to the server!\n')

client.settimeout(0)
client.setblocking(1)

def receive_messages():
    """
    Receives messages from the server
    """
    
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
        except:
            print('An error occured!')
            client.close()
            break

def write_messages():
    """
    Sends messages to the server
    """

    while True:
        message = input()
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()
