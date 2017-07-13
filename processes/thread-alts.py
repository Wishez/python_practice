import _thread as thread
import sys, time

firstArg = sys.argv[1]

def action(i):
	print(int(i) ** 32)

class Power:
	def __init__(self, i):
		self.i = int(i)
	def action(self):
		print(self.i ** 32)

if __name__ == '__main__':
	print('start')
	thread.start_new_thread(action, (firstArg,))
	thread.start_new_thread(lambda: action(firstArg), ())
	obj = Power(firstArg)
	thread.start_new_thread(obj.action, ())
	time.sleep(1)
	print('end')



