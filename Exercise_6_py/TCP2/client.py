import sys
from socket import *
from lib import Lib

HOST = ''
PORT = 9000
BUFSIZE = 1000

def main(argv):

    clientSocket = socket(AF_INET, SOCK_STREAM)
    HOST = '10.0.0.1'
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
