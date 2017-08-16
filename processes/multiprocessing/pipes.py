from multiprocessing import Pipe, Process


def sender(pipe):
	pipe.send(['spam'] + ['Hello,', 'Dude.'])
	pipe.close()


def talker(pipe):
	pipe.send(dict(name='Hurry', age=11, work='Dark Lord'))
	reply = pipe.recv()
	print('See spam:', reply)


if __name__ == '__main__':
	(parentEnd, childEnd) = Pipe()

	Process(target=sender, args=(childEnd,)).start()

	print('Parent got:', parentEnd.recv())
	parentEnd.close()

	(parentEnd, childEnd) = Pipe()

	child = Process(target=talker, args=(childEnd,))
	child.start()
	print('Another one parent got:', parentEnd.recv())
	parentEnd.send({x * 2 for x in 'spam'})
	child.join()

