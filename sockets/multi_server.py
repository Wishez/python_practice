# -*- encoding: utf-8 -*-
from fork_socket import *
from multiprocessing import Process

def handleClient(connection):
	# time.sleep(self.timeout)
	while True:
		data = connection.recv(1024)
		if not data: break
		reply = 'Echo=>%s at %s' % (data, self.now())
		connection.send(reply.encode())
	connection.close()

class MultyServer(ForkSocket):
	def __init__(self, host='', port=PORT, timeout=5.0):
		self.host = host
		self.port = port
		self.sock = ''
		self.timeout = timeout

		ForkSocket.__init__(self)
		# self.activeChildren = []
	# Killing a children process, when it'll had completed its work.
	# def reapChildren(self):
	# 	while self.activeChildren:
	# 		pid, stat = os.waitpid(0, os.WNOHANG)
	# 		print(pid, stat, os.WNOHANG)
	# 		if not pid: break
	# 		self.activeChildren.remove(pid)

	def dispatcher(self):
		while True:
			connection, address = self.sock.accept()
			print('Server connected by', address)
			print('at', self.now())
			Process(target=handleClient, args=(connection,)).start()
			if childPid == 0:
				self.handleClient(connection)

if __name__ == '__main__':
	

	if sys.argv[1] == 'serve':
		forkSocket = ForkSocket()
		forkSocket()
	else:
		cs = ConnectSocket(sys.argv[1])
		threads = []
		for x in range(50):
			time.sleep(0.5)
			thread = Thread(target=cs, args=(sys.argv[2:],))
			threads.append(thread)
			thread.start()

		for thread in threads:
			thread.join()
# python multi_server.py shining-present.ru
# # python multi_server.py serve
# cd /scripts/python_practice/sockets