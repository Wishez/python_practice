# -*- encoding: utf-8 -*-
import os, sys, time, threading
childfifo = '/tmp/childfifo'
parentfifo = '/tmp/parentfifo'

def child():
	# открывает fifo дескриптор для чтения и записи
	pipeout = os.open(parentfifo, os.O_WRONLY) 
	pipein = open(childfifo, 'r')
	zzz = 1

	while True:
		time.sleep(zzz)
		# был открыт в двоичном режиме.
		msg = ('Spam %03d\n' % zzz).encode()
		os.write(pipeout, msg)
		
		line = pipein.readline()[:-1]
		if line:
			print('Child %d got "%s" at %s.' % (os.getppid(), line, time.time()))
		
	os._exit()

if __name__ == '__main__':
	if os.path.exists(childfifo):
		os.remove(childfifo)
	os.mkfifo(childfifo)
	child()
