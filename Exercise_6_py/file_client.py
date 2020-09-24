import sys
from socket import *
from lib import Lib

NAME = "10.0.0.1"
PORT = 9000
BUFSIZE = 1000

def main(argv):
	clientSocket = socket(AF_INET, SOCK_STREAM)
	print("Klient connecter...")
	clientSocket.connect((NAME, PORT))
	print("Klient connected.")
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
