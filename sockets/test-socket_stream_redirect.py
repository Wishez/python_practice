import sys, os, multiprocessing
from socket_stream_redirect import *

sd = Screwdriver()

def server1():
	mypid = os.getpid()
	conn = sd.initListenerSocket()
	file = conn.makefile('r')
	for i in range(3):
		data = file.readline().rstrip()
		print('server %s got [%s]' % (mypid, data))

def client1():
	mypid = os.getpid()
	sd.redirectOut() 
	for i in range(3):
		print('client %s: %s' % (mypid, i))
		sys.stdout.flush()

def server2():
	mypid = os.getpid()
	conn = sd.initListenerSocket()
	for i in range(3):
		conn.send(('server %s: %s\n' % (mypid, i)).encode())

def client2():
	mypid = os.getpid()
	sd.redirectIn()
	for i in range(3):
		data = input()
		print('client %s got [%s]' % (mypid, data))

def server3():
	mypid = os.getpid()
	conn = sd.initListenerSocket()
	file = conn.makefile('r')
	for i in range(3):
		data = file.readline().rstrip()
		conn.send(('server %s got [%s]\n' % (mypid, data)).encode())

def client3():
	mypid = os.getpid()
	sd.redirectBothAsClient()
	for i in range(3):
		print('client %s: %s' % (mypid, i))
		data = input()
		sys.stderr.write('client %s got [%s]\n' % (mypid, data))

def server4():
	mypid = os.getpid()
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((self.host, self.port))
	file = sock.makefile('r')
	for i in range(3):
		sock.send(('server %s: %s\n' % (mypid, i)).encode())
		data = file.readline().rstrip()
		print('server %s got [%s]' % (mypid, data))

def client4():
	mypid = os.getpid()
	sd.redirectBothAsServer()
	for i in range(3):
		data = input()
		print('client %s got [%s]' % (mypid, data))
		sys.stdout.flush()

def server5():
	mypid = os.getpid()
	conn = sd.initListenerSocket()
	file = conn.makefile('r')
	for i in range(3):
		conn.send(('server %s: %s\n' % (mypid, i)).encode())
		data = file.readline().rstrip()
		print('server %s got [%s]' % (mypid, data))

def client5():
	mypid = os.getpid()
	sd.redirectBothAsClient()
	for i in range(3):
		data = input()
		print('client %s got [%s]' % (mypid, data))
		sys.stdout.flush()
		
if __name__ == '__main__':
	num = sys.argv[1]
	server = eval('server' + num)
	client = eval('server' + num)
	multiprocessing.Process(target=server).start()

	client()