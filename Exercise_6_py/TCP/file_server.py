#!/usr/bin/python3

import sys
import socket

HEADER = 1000
SERVER = socket.gethostbyname(socket.gethostname()) # local ip
PORT = 9000
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

#def sendFile(fileName,  fileSize,  conn):
	# TO DO Your Code

if __name__ == "__main__":
	main(sys.argv[1:])
