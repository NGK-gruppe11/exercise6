#!/usr/bin/python3

import sys
import socket
from lib import Lib # har en funktion til at returnere size af fil

HEADER = 1000 # bytes der skal sendes pr gang
SERVER = "192.168.8.101" # local ip
PORT = 5050
ADDR = (SERVER, PORT) # adresse består af ip + port
FORMAT = 'utf-4'

def main(argv):

	print("Server set to ", ADDR)
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # setup server som ipv4 og tcp

	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # ingen ventetid når server genstartes

	server.bind(ADDR) # bind addresse og server sammen
	server.listen() # lyt efter klienter

	while 1:
		print("Server er klar.")
		conn, addr = server.accept() # blokerende funktion der venter indtil listen() opfanger en klient
		print("Socket accept", addr) # print klient

		msg = conn.recv(HEADER) # blokerende linje der venter til besked er modtaget (fil navnet)
		print("Besked modtaget fra klient:", msg.decode()) # decode() konvertere besked til string
		
		sendFile(msg.decode(), conn) # send fil (msg) til klient(conn)

		conn.close()

def sendFile(fileName, conn):
	try:
		# prøv at sende størrelse af fil...
		msg = "File size: " + str(Lib.check_File_Exists(fileName))
		conn.send(msg.encode())
	except:
		# hvis det mislykkes. send en fejl besked
		conn.send("File not found!".encode())

	with open(fileName, "rb") as file: # åben fil
		data = file.read(HEADER) # læs de første 1000 bytes
		print("Sending...")
		while data: # læs data indtil der ikke er mere
			conn.send(data) # send til klient
			data = file.read(HEADER) # læs næste 1000 bytes
	print("File sent.")

if __name__ == "__main__":
	main(sys.argv[1:])
