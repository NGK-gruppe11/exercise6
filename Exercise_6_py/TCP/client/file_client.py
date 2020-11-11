#!/usr/bin/python3

import sys
import socket
from lib import Lib

HEADER = 1000
SERVER = "10.0.0.1" # ip på server
PORT = 9000
ADDR = (SERVER, PORT)

def main(argv):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Klient connecter til ", ADDR)

	client.connect(ADDR) # connect til server
	print("Klient connected.")
	fileMsg = input("Input: ") # få terminal input (fil)

	# file size
	client.sendto(fileMsg.encode(), ADDR) # send navn på fil. encode() konvertere besked til bits
	bytesAdrPair = client.recvfrom(HEADER) # modtag besked fra server (size af fil)
	msgFromServer = bytesAdrPair[0] # selve besked ligger på index 0
	print(msgFromServer.decode()) # print size af fil (eller fejl besked)

	# receive file
	with open(fileMsg, "wb") as file: # lav ny fil på klient
		print("Getting file...")
		while True:
			data = client.recv(HEADER) # modtag besked 1000 bytes ad gangen
			file.write(data) # skriv modtaget data til egen fil
			if not data: # hvis der ikke er mere data...
				break # bryd loop

		print("File received.")
	client.close()

if __name__ == "__main__":
   main(sys.argv[1:])
