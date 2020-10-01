import sys
import socket
from lib import Lib

HOST = ''
PORT = 9000
BUFSIZE = 1000

def main(argv):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = socket.gethostname()
    serverSocket.bind((HOST,PORT))
    serverSocket.listen(1)
    
    print 'Server is listening... '

    while True:
        connectionSocket, addr = serverSocket.accept()
        print 'Connection from' , addr, 'has been established'
        data = connectionSocket.recv(1024)
        print ('Server ready to send...', repr(data))
        print ('Enter name of file: ')
        filename = raw_input("") #skal matche det korrekte fil navn
        file = open(filename, "rb")
        data = file.read(BUFSIZE)
        while(data):
            send = connectionSocket.send(data)
            print ('Sent', repr(data))
            data = file.read(BUFSIZE)


        file.close()

        print ('Send Complete!')
        connectionSocket.close()
        print ('Closing down connectionSocket...')


if __name__ == "__main__":
    main(sys.argv[1:])
    