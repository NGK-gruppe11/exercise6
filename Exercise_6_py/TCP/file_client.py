#!/usr/bin/python3

import sys
import socket

HEADER = 1000
SERVER = "127.0.1.1"
PORT = 9000
ADDR = (SERVER, PORT)

def main(argv):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Klient connecter...")

	client.connect((SERVER, PORT))
	print("Klient connected.")
	msgToServer = input("Input: ")

	client.sendto(msgToServer.encode(), (SERVER, PORT))
	bytesAdrPair = client.recvfrom(HEADER)
	msgFromServer = bytesAdrPair[0]
	print(msgFromServer.decode())
	client.close()

if __name__ == "__main__":
   main(sys.argv[1:])
