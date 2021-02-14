import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 3000

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    
    print("received connection from " % str(address))
    
    message = 'hello world!' + "\r\n"
    clientsocket.send(message)
    
    clientsocket.close()
    