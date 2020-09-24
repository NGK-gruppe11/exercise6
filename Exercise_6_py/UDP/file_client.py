#!/usr/bin/python3

import sys
from socket import socket, AF_INET, SOCK_DGRAM

PORT = 9000

def main(argv):
	NAME = "192.168.199.137"

	print("Klient connecter...")
	clientSocket = socket(AF_INET, SOCK_DGRAM)

	msgToServer = input("Input: ")
	clientSocket.sendto(msgToServer.encode(), (NAME, PORT))
	bytesAdrPair = clientSocket.recvfrom(2048)
	
	msgFromServer = bytesAdrPair[0]
	print(msgFromServer.decode())
	clientSocket.close()
    
#def receiveFile(fileName,  conn):
	# TO DO Your Code

if __name__ == "__main__":
   main(sys.argv[1:])
