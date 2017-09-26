import sys
from socket import *

PORT = 50009
HOST = 'localhost'

class Screwdriver():
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port

    def initListenerSocket(self):
        print('Start')
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind(('', self.port))
        sock.listen(5)
        conn, add = sock.accept()
        return conn
    def redirectOut(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((self.host, self.port))
        file = sock.makefile('w')
        sys.stdout = file
        return sock

    def redirectIn(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((self.host, self.port))
        file = sock.makefile('r')
        sys.stdin = file
        return sock
    def redirectBothAsClient(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((self.host, self.port))
        ofile = sock.makefile('w')
        ifile = sock.makefile('r')
        sys.stdin = ifile
        sys.stdout = ofile
        return sock

    def redirectBothAsServer(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(5)
        conn, add = sock.accept()
        ofile = sock.makefile('w')
        ifile = sock.makefile('r')
        sys.stdin = ifile
        sys.stdout = ofile
        return conn
