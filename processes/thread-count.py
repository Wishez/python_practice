import sys, time
import _thread as thread


class ProcessesCounter:
	def __init__(self, quantityProcesses, count):
		self.count = int(count)
		self.quantityProcesses = int(quantityProcesses)
		self.totalExecutedProcesses = 0

	def counter(self, processId):
		for i in range(self.count):
			time.sleep(1)
			print('[%s] => %s' % (processId, i))
			self.totalExecutedProcesses += 1

	def startCount(self):
		for i in range(self.quantityProcesses):
			thread.start_new_thread(self.counter, (i,))
	def showTimeExecutingProcesses(self, seconds):
		for i in range(seconds):
			time.sleep(1)
			print('Ending in %s' % (seconds - i))

if __name__ == '__main__':
	quantityProcesses = sys.argv[1]
	count = sys.argv[2]

	processesCounter = ProcessesCounter(quantityProcesses, count)

	timeExecuting = int(count)
	thread.start_new_thread(processesCounter.showTimeExecutingProcesses, ((timeExecuting - 1),))
	processesCounter.startCount()
	time.sleep(timeExecuting)

	print('Total processes were %s' % processesCounter.totalExecutedProcesses)
	print('Close!')