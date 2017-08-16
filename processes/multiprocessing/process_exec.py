from multiprocessing import Process
import os, time, sys

def startChild(arg):
	print('Thread process => %s' % os.getpid())
	os.execlp('python', 'python', 'child.py', str(arg))


if __name__ == '__main__':
	for i in range(5):
		print('Parent => %s' % os.getpid())
		process = Process(target=startChild, args=(i,))
		# process.daemon = True
		process.start()

	print('Exit...')