# -*- encoding: utf-8 -*-
import os, time, queue, multiprocessing, sys

class Counter(multiprocessing.Process):
	label = "@"
	def __init__(self, state, queue):
		self.state = state
		self.post = queue
		multiprocessing.Process.__init__(self)

	def run(self):
		for i in range(3):
			time.sleep(1)
			self.state += 1
			print(self.label, self.pid, self.state)
			self.post.put([self.pid, self.state])

		print(self.label, self.pid, '-')


if __name__ == '__main__':
	print('start', os.getpid())
	expected = 9

	post = multiprocessing.Queue()

	q = Counter(0, post)
	w = Counter(100, post)
	e = Counter(1000, post)
	q.start(); w.start(); e.start()
	while expected:
		try: 
			data = post.get(block=False)
		except queue.Empty:
			time.sleep(1.5)
			print('no data...')
		else:
			print('posted:', data)
			expected -= 1

	q.join(); w.join(); e.join()
	# exitcode - код завершения потомка
	print('finish', os.getpid(), e.exitcode)
