import sys
from socket import socket, AF_INET, SOCK_DGRAM

PORT = 9000

def main(argv):
	NAME = "10.0.0.1"

	print("Klient connecter...")
	clientSocket = socket(AF_INET, SOCK_DGRAM)

	msgToServer = input("Input: ")
	clientSocket.sendto(msgToServer.encode(), (NAME, PORT))
	bytesAdrPair = clientSocket.recvfrom(2048)
	
	msgFromServer = vytesAdrPair[0]
	print(msgFromServer.decode())
	clientSocket.close()
    
def receiveFile(fileName,  conn):
	# TO DO Your Code

if __name__ == "__main__":
   main(sys.argv[1:])
