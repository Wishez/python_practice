# -*- encoding: utf-8 -*-
import time, sys
HOST = ''
from fork_socket import PORT
from  SocketServer import ThreadingTCPServer, BaseRequestHandler

def now():
	return time.asctime()

class MyHandler(BaseRequestHandler):
	def handle(self):
		print(self.client_address, now())
		while True:
			data = self.request.recv(1024)
			if not data: break
			reply = 'Echo=> %s, you send it at %s' % (data, now())
			self.request.send(reply.encode())
		self.request.close()

if __name__ == '__main__':
	address = (HOST, PORT,)
	server = ThreadingTCPServer(address, MyHandler)

	server.serve_forever()