# -*- encoding: utf-8 -*-
import os, sys, time, threading
parentfifo = '/tmp/parentfifo'
childfifo = '/tmp/childfifo'

def parent():
	# Открывает fifo в текстовом режиме.
	pipein = open(parentfifo, 'r') 
	# Именнованный канал на запись.
	pipeout = os.open(childfifo, os.O_WRONLY)
	# Ожидание данных от дочерней фкен
	while True:
		line = pipein.readline()[:-1]
		print('Parent %d got "%s" at %s' % (os.getpid(), line, time.time()))
		# Запись в именованный канал из которого будет читать функция child,
		# а если точнее, то его порождёный поток succesMeessageToChild ожидающий
		# поступления данных в именованный канал. 
		msg = ('I get your data, son.\n').encode()
		os.write(pipeout, msg)


if __name__ == '__main__':
	if os.path.exists(parentfifo):
		os.remove(parentfifo)
	os.mkfifo(parentfifo)
	parent()