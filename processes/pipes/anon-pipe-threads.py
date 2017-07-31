# -*- encoding: utf-8 -*-

import threading, time, os

def child(pipeout):
	zzz = 0
	while True:
		time.sleep(zzz)
		msg = ('Spam %03d\n' % zzz).encode()
		os.write(pipeout, msg)
		zzz = (zzz+1) % 5

def parent(pipein):
	while True:
		line = pipein.readline()[:-1]
		print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


if __name__ == "__main__":
	pipein, pipeout = os.pipe()
	threading.Thread(target=child, args=(pipeout,)).start()
	pipein = os.fdopen(pipein)
	parent(pipein)

#cd C:\Users\Shining\dev\python_practice\processes\pipes
# python anon-pipe-threads.py