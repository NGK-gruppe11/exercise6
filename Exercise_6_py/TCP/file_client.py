#!/usr/bin/python3

import sys
from socket import socket, AF_INET, SOCK_STREAM

NAME = "192.168.199.137"
PORT = 9000

def main(argv):
	clientSocket = socket(AF_INET, SOCK_STREAM)
	print("Klient connecter...")
	clientSocket.connect((NAME, PORT))
	print("Klient connected.")
	msgToServer = input("Input: ")
	clientSocket.sendto(msgToServer.encode(), (NAME, PORT))
	bytesAdrPair = clientSocket.recvfrom(2048)
	msgFromServer = bytesAdrPair[0]
	print(msgFromServer.decode())

	# receive file

	l = clientSocket.recv(1024)
	while(l)
			f.write(l)
			l = clientSocket.recv(1024)

	##############

	clientSocket.close()
    
# def receiveFile(fileName,  conn):
	# TO DO Your Code

if __name__ == "__main__":
   main(sys.argv[1:])
