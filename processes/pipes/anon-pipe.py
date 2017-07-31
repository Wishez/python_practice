# -*- encoding: utf-8 -*-
import os, time

def child(pipeout):
	zzz = 0
	while True:
		time.sleep(zzz)
		msg = ('Spam %03d' % zzz).encode()
		os.write(pipeout, msg)
		zzz = (zzz+1) % 5

def parent():
	pipein, pipeout = os.pipe()
	if os.fork() == 0:  # проверка на родительский процесс
		child(pipeout) # создание дочернего ответвлнного процесса
	else:
		while True:
			line = os.read(pipein, 32)  # чтение выходного дескриптора файла
			print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


if __name__ == '__main__':
	parent()