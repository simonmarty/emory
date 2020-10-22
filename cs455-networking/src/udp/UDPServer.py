# UDPServer.py

import socket

PORT = 12000
serverSocket = socket.socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', PORT))
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode().upper()
    serverSocket.sendto(message.encode(), clientAddress)