import sys
from socket import *
from lib import Lib

HOST = '192.168.199.137'
PORT = 9000
BUFSIZE = 1000

def main(argv):

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((HOST,PORT))
    clientSocket.send("Greetings")

    print ('Ready to receive...')

    with open('received_file.jpeg','wb') as file:
        print 'File opened...'
        while True:
            print ('Receiving Data...')
            data = clientSocket.recv(BUFSIZE)
            print('data=%s',(data))
            if not data:
                break
            file.write(data)
        file.close()

        print ('File successfully received!')

        clientSocket.close()

        print ('Connection closed...')

if __name__ == "__main__":
    main(sys.argv[1:])
