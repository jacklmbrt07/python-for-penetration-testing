import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.1.104
host = socket.gethostname()
port = 3000

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    
    print("received connection from %s " % str(address))
    
    message = 'hello world!' + "\r\n"
    clientsocket.send(message.encode('ascii'))
    
    clientsocket.close()
    