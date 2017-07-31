import _thread as thread
exitstat = 0

def child():
	global exitstat
	exitstat += 1
	threadid = thread.get_ident()
	print('Hello from child', threadid, exitstat)
	thread.exit()
	print('I never will be displayed')

def parent():
	while True:
		thread.start_new_thread(child, ())
		if input() == 'q': break

if __name__ == '__main__': parent()