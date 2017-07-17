import sys, time
import _thread as thread


class ProcessesCounter:
	def __init__(self,
		 quantityProcesses,
		 count,
		 mutex=thread.allocate_lock()
	):
		self.count = int(count)
		self.quantityProcesses = int(quantityProcesses)
		self.totalExecutedProcesses = 0
		self.mutex = mutex
		self.exitmutexes = [False] * 10
	def counter(self, processId):
		for i in range(self.count):
			self.mutex.acquire()
			print('[%s] => %s' % (processId, i))
			self.totalExecutedProcesses += 1
			self.mutex.release()
		self.exitmutexes[processId] = True

	def startCount(self):
		for i in range(self.quantityProcesses):
			thread.start_new_thread(self.counter, (i,))
		while False in self.exitmutexes: pass

if __name__ == '__main__':
	quantityProcesses = sys.argv[1]
	count = sys.argv[2]
	processesCounter = ProcessesCounter(quantityProcesses, count)
	
	processesCounter.startCount()
	

	print('Total processes were %s' % processesCounter.totalExecutedProcesses)
	print('Main thread exiting.')