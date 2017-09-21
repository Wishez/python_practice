import sys, time
from select import select 
from socket import socket, AF_INET, SOCK_STREAM

def now():
	return time.ctime(time.time())

myHost = ''
myPort = 50000

if len(sys.argv) == 3:
	myHost, myPort = sys.argv[1:]
numPortSocks = 2 # Quantity of ports for clients connecting

# Create main sockets for accept new requests to connecting from clients
mainsocks, readsocks, writesocks = [], [], [] 
for i in range(numPortSocks):
	portsock = socket(AF_INET, SOCK_STREAM)
	portsock.bind((myHost, myPort))
	portsock.listen(5)
	mainsocks.append(portsock) # Add to the main list for identification

	readsocks.append(portsock) # Add to the list of source of select
	myPort += 1

# loop of events: listen and multiplexing while a process isn't completed
# 
print('select-server loop starting')
while True:
	readables, writeables, exceptions = select(readsocks, writesocks, [])
	for sockobj in readables: # for prepered entry sockets
		if sockobj in mainsocks:
			# socket of a port: acceptp connection from a new client
			newsock, address = sockobj.accept()

			print('Connect:', address, id(newsock))
			readsocks.append(newsock)
		else:
			# socket of client: read next string
			data = sockobj.recv(1024) # recv havn't to block smth
			print('\tgot', data, 'on', id(sockobj))
			if not data: # if client close it
				sockobj.close() # close and remove from list
				readsocks.remove(sockobj) # else it will be served of select execution
			else: 
				reply = 'Echo=>%s at %s' % (data, now())
				sockobj.send(reply.encode())

		
