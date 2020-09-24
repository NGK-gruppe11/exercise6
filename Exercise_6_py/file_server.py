import sys
import socket
from lib import Lib

HOST = ''
PORT = 9000
BUFSIZE = 1000

def main(argv):
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.bind((HOST, PORT))
	serverSocket.listen(1)

	while 1:
		print("Server er klar.")
		connectionSocket, addr = serverSocket.accept()
		print("Socket accept", addr)

		msg = connectionSocket.recv(2048)
		print("Besked modtaget fra klient:", msg.decode())
		msg = msg.upper()
		connectionSocket.send(msg)
		connection.close()

def sendFile(fileName,  fileSize,  conn):
	# TO DO Your Code
    
if __name__ == "__main__":
   main(sys.argv[1:])
