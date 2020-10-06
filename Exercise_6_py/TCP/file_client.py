#!/usr/bin/python3

import sys
from socket import socket, AF_INET, SOCK_STREAM

HEADER = 1000
CLIENT = socket.gethostbyname(socket.gethostname())
PORT = 9000
ADDR = (CLIENT, PORT)

def main(argv):
	clientSocket = socket(AF_INET, SOCK_STREAM)
	print("Klient connecter...")

	clientSocket.connect(ADDR)
	print("Klient connected.")
	msgToServer = input("Input: ")
	
	clientSocket.sendto(msgToServer.encode(), ADDR)
	bytesAdrPair = clientSocket.recvfrom(HEADER)
	msgFromServer = bytesAdrPair[0]
	print(msgFromServer.decode())
	clientSocket.close()

if __name__ == "__main__":
   main(sys.argv[1:])
