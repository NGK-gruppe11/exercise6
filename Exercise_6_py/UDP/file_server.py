#!/usr/bin/python3

import sys
import os
from socket import socket, AF_INET, SOCK_DGRAM

HOST = ""
PORT = 9000

def main(argv):
	UDPServerSocket = socket(AF_INET, SOCK_DGRAM)
	UDPServerSocket.bind((HOST, PORT))
	
	print("Server er klar.")

	while 1:
		bytesAdrPair = UDPServerSocket.recvfrom(2048)
		msg = bytesAdrPair[0]
		
		clientAdr = bytesAdrPair[1]
		print("Besked modtaget fra klient", clientAdr, ":", msg.decode())
		msg = msg.upper()
		UDPServerSocket.sendto(msg, clientAdr)
		
#def sendFile(fileName,  fileSize,  conn):
	# TO DO Your Code
    
if __name__ == "__main__":
  	main(sys.argv[1:])
