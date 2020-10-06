#!/usr/bin/python3

import sys
import socket
from lib import Lib

HEADER = 1000
SERVER = "192.168.199.137" # local ip
PORT = 5050
ADDR = (SERVER, PORT)

def main(argv):

	print("Server set to ", ADDR)
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	server.bind(ADDR)
	server.listen()

	while 1:
		print("Server er klar.")
		conn, addr = server.accept()
		print("Socket accept", addr)

		msg = conn.recv(HEADER)
		print("Besked modtaget fra klient:", msg.decode())
		msg = msg.upper()

		conn.send(msg)
		conn.close()

def sendFile(fileName,  fileSize,  conn):
	pass

if __name__ == "__main__":
	main(sys.argv[1:])
