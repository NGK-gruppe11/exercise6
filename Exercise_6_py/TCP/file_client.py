#!/usr/bin/python3

import sys
import socket

HEADER = 1000
SERVER = "192.168.199.137"
PORT = 9000
ADDR = (SERVER, PORT)

def main(argv):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Klient connecter...")

	client.connect(ADDR)
	print("Klient connected.")
	msgToServer = input("Input: ")

	client.sendto(msgToServer.encode(), ADDR)
	bytesAdrPair = client.recvfrom(HEADER)
	msgFromServer = bytesAdrPair[0]
	print(msgFromServer.decode())
	client.close()

if __name__ == "__main__":
   main(sys.argv[1:])
