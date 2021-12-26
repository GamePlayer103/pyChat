# pyChat
Command line chatting app written in python.

## Usage
#### Setting server ip and port
Find and open your `server.py` file. At the top of the file you should find two config variables. Change them as you want.
```
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 1234
```

### Using the server
To start the server run `python3 server.py` in your server's folder.

### Connecting client to the server
To connect to the server type `python3 client.py <server ip> <server_port>` in your client's folder.

## Todo
- [x] Basic sending and reciving messages
- [ ] Client's ui improvement
- [ ] Nicknames
- [ ] Better readme
