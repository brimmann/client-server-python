from socket import *
serverPort = 9080
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((b'', serverPort))
print("The server is ready to recive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("It is me")
    print(clientAddress)
    print("Message Arrived: " + message.decode())
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    
