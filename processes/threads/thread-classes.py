import threading 

class Mythread(threading.Thread): # наследуется от класса Thread
	def __init__(self, myId, count, mutex): 
		#  информация для каждого потока
		#  совместно используемые объекты,
		#  вместо глобальных переменных
		self.myId = myId
		self.count = count 
		self.mutex = mutex
		threading.Thread.__init__(self)
	def run(self):
		for i in range(self.count): 
			with self.mutex: 
				print('[%s] => %s' % (self.myId, i))


stdoutmutex = threading.Lock()
threads = []
for i in range(10):
	thread = Mythread(i, 100, stdoutmutex)
	thread.start()
	threads.append(thread)

for thread in threads:
	thread.join()
print('Main thread exiting.')