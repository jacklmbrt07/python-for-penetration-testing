import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.1.104'
host = socket.gethostname()

port = 3000

clientsocket.connect((host, port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
