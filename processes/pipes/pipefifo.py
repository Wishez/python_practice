# -*- encoding: utf-8 -*-
"""
	Эта программа реализует взаимодействие между программ, применяя именованные
	каналы. Именованные каналы - каналы, которые действуют примерно также,
	как и анонимные каналы, за исключением того, что они создают файл в файловой
	системе, а не просто используют временный дескриптор файла для каналов. Этот
	способ взаимодействия, используется для обменна данных между разными программами,
	к примеру, программами клиента и сервер. Каналы - однопоточны, но чтобы использовать
	двунаправленные трубы для обмена данными в обоих направлениях, с клиента серверу и
	с сервера клиента, можно создавать два канала fifo, а следовательно два файла
	в файловой системе.
"""
import os, sys, time, threading
parentfifo = '/tmp/forparentread'
childfifo = '/tmp/forchildread'


def child():
	# открывает fifo дескриптор для чтения и записи
	pipeout = os.open(parentfifo, os.O_WRONLY) 
	zzz = 0

	while True:
		time.sleep(zzz)
		# был открыт в двоичном режиме.
		msg = ('Spam %03d\n' % zzz).encode()
		os.write(pipeout, msg)
		zzz = (zzz+1) % 5

def parent():
	# Открывает fifo в текстовом режиме.
	pipein = open(parentfifo, 'r') 
	# Ожидание данных от дочерней фкен
	while True:
		line = pipein.readline()[:-1]
		print('Parent %d got "%s" at %s' % (os.getpid(), line, time.time()))

if __name__ == '__main__':
	
	os.mkfifo(parentfifo)

	if len(sys.argv) == 1:
		parent()
	else:
		child()