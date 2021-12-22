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
print("Connecting to the server...")

try:
    client.connect((server_ip, server_port))
except socket.error as error:
    print('Connection error: ' + str(error))
