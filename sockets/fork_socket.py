# -*- encoding: utf-8 -*-
import os, sys, time
from socket import *
from threading import Thread
#from signal import signal, SIG_IGN, SIGCHLD
PORT = 50000

class ForkSocket():
	def __init__(self, host='', port=PORT, timeout=5.0):
		self.host = host
		self.port = port
		self.sock = ''
		self.timeout = timeout
		# self.activeChildren = []
	# Killing a children process, when it'll had completed its work.
	
	def now(self):
		return time.ctime(time.time())

	# def reapChildren(self):
	# 	while self.activeChildren:
	# 		pid, stat = os.waitpid(0, os.WNOHANG)
	# 		print(pid, stat, os.WNOHANG)
	# 		if not pid: break
	# 		self.activeChildren.remove(pid)

	def handleClient(self, connection):
		# time.sleep(self.timeout)
		while True:
			data = connection.recv(1024)
			if not data: break
			reply = 'Echo=>%s at %s' % (data, self.now())
			connection.send(reply.encode())
		connection.close()

	def __call__(self):
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.bind((self.host, self.port))
		self.sock.listen(5)
		signal(SIGCHLD, SIG_IGN)
		self.dispatcher()

	def dispatcher(self):
		while True:
			connection, address = self.sock.accept()
			print('Server connected by', address)
			print('at', self.now())
			# self.reapChildren()
			childPid = os.fork()
			if childPid == 0:
				self.handleClient(connection)


class ConnectSocket():
	def __init__(self, host='', port=PORT, timeout=5.0):
		self.host = host
		self.port = port
		self.sock = ''
		self.timeout = timeout

	def __call__(self, text):
		self.sock = socket(AF_INET, SOCK_STREAM)

		self.sock.connect((self.host, self.port))
		self.sock.send(('%s' % text).encode())
		while True:
			data = self.sock.recv(1024)
			if not data: break
			print(data)
		self.sock.close()

if __name__ == '__main__':
	

	if sys.argv[1] == 'serve':
		forkSocket = ForkSocket()
		forkSocket()
	else:
		cs = ConnectSocket(sys.argv[1])
		threads = []
		for x in range(60):
			# time.sleep(0.5)
			thread = Thread(target=cs, args=(sys.argv[2:],))
			threads.append(thread)
			thread.start()

		for thread in threads:
			thread.join()
# python fork_socket.py shining-present.ru
# cd /scripts/python_practice/sockets