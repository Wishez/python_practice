# -*- encoding: utf-8 -*-
import os, time

def child(pipeout):
	zzz = 0
	while True:
		time.sleep(zzz)
		# Файловый дескриптор будет оборачиваться в объект файла,
		# из которого можно будет вытаскивать построчную информацию
		# при помощи функции файла readline
		msg = ('Spam %03d\n' % zzz).encode() 
		os.write(pipeout, msg)
		# Считает до 5 вызовов, после сбрасывается.
		zzz = (zzz+1) % 5

def parent():
	pipein, pipeout = os.pipe()
	if os.fork() == 0:  # проверка на родительский процесс
		child(pipeout) # создание дочернего ответвлнного процесса
	else:

		os.close(pipeout)
		pipein = os.fdopen(pipein)
		while True:
			line = pipein.readline()[:-1]  # чтение выходного дескриптора файла
			print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


if __name__ == '__main__':
	parent()