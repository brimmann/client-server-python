from socket import *
serverName = b'127.0.0.1'
serverPort = 9080
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('Enter a sentences: ')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    
