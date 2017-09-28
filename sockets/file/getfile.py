import sys, os, time, _thread as thread 
from socket import *

blksz = 1024
defaultHost = 'localhost'
defaultPort = 44234

helptext = """
server=> getfile.py -mode server    [-port nnn] [-host hhh|localhost]
client=> getfile.py [-mode client] -fole fff [-port nnn] [-host hhh|localhost]
"""
# A simple interface is based on socket and using for transpartation
# a file from a server to a client.  
class FileGetter:
	def __init__(self, host=defaultHost, port=defaultPort, timeout=5):
		self.host = host
		self.port = port
		self.timeout = timeout
		self.cl_sock = ''
		self.s_sock = ''
	def now(self):
		return time.ctime(time.time())
	# Return cmd parametrs like a dictionary when the programm is executing.
	def parsecommandline(slef):
		dict = {}
		args = sys.argv[1:]
		while len(args) >= 2:
			dict[args[0]] = args[1]
			args = args[2:]
		return dict
	# Raise a client socket and ask for a file.
	def client(self, filename):
		self.cl_sock = socket(AF_INET, SOCK_STREAM)
		self.cl_sock.connect((self.host, self.port))
		self.cl_sock.send((filename + '\n').encode())
		dropdir = os.path.split(filename)[1]
		file = open(dropdir, 'wb')
		while True:
			data = self.cl_sock.recv(blksz)
			if not data: break
			file.write(data)
		cl_sock.close()
		file.close()

		print('Client got', filename, 'at', self.now())

	# Take client socket was gotten 
	# and write to a client's socket-file data in byte format.
	def serverthread(self, clientsock):
		sockfile = clientsock.makefile('r')
		filename = sockfile.readline()[:-1]

		try:
			file = open(filename, 'rb')
			while True:
				bytes = file.read(blksz)
				if not bytes: break
				sent = clientsock.send(bytes)
				assert sent == len(bytes)
		except:
			print('Error downloading file on server:', filename)
		clientsock.close()

	def server(self):
		self.s_sock = socket(AF_INET, SOCK_STREAM)
		self.s_sock.bind(('', self.port))
		self.s_sock.listen(5)
		while True:
			clientsock, clientaddr = self.s_sock.accept()
			print('Server connected by', clientaddr, 'at', self.now())
			thread.start_new_thread(self.serverthread, (clientsock,))
	# Deploy servers by options. 
	def main(self, args):
		self.host = args.get('-host', defaultHost)
		self.port = int(args.get('-port', defaultPort))
		if args.get('-mode') == 'server':
			if self.host == 'localhost': self.host = ''
			self.server()
		elif args.get('-file'):
			self.client(args['-file'])
		else:
			print(helptext)

if __name__ == '__main__':
	fg = FileGetter()
	args = fg.parsecommandline()
	fg.main(args)

