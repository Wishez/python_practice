numconsumers = int(input('Quantity consumers => ')) # Quantitity of thread-comsumers
numproducers = int(input('Quantity producers => ')) # Quantitity of thread-producers 
import threading, queue, time, sys


nummessages = int(input('Number of messages making by producers => '))  # Quantitity of messages producer fits 
safeprint = threading.Lock() # в противном случае вывод может
								   # перемешиваться

dataQueue = queue.Queue() # Common queue of unlimited size

def producer(idnum):
	for msgnum in range(nummessages):
		with safeprint:
			dataQueue.put('[producer id=%d, count=%d]' % (idnum, msgnum))

def consumer(idnum):
	while True:
		time.sleep(0.1)
		try:
			data = dataQueue.get(block=False)
		except queue.Empty:
			sys.exit()
		else:
			with safeprint:
				print ('consumer', idnum, 'got data =>', data)
				
if __name__ == '__main__':
	for i in range(numconsumers):
		thread = threading.Thread(target=consumer, args=(i,))
		thread.deamon = True
		thread.start()

	waitfor = []
	for i in range(numproducers):
		thread = threading.Thread(target=producer, args=(i,))
		waitfor.append(thread)
		thread.start()

	for thread in waitfor:
		thread.join()
	

# python queuetest.py
