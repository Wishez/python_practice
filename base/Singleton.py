from random import randint

class Lego(type):
	instance = None
	def __call__(cls, *arg, **kw):
		if not cls.instance:
			cls.instance = super(Lego, cls).__call__(*arg, **kw)
		return cls.instance



class Worker(metaclass=Lego):
	def __init__(self, sizeOfCaste=10):
		self.blocks = 0
		self.sizeOfCaste = sizeOfCaste

	def successMessage(self):
		return 'Yeah! You did it!'

	def failureMessage(self):
		return 'It\'s time to start to build your own castle!'

	def isCastleBuilded(self):
		progress = self.blocks * self.sizeOfCaste

		print('Current progress of building your castle is: %s percents.' % progress)
		if progress == 0:
			self.failureMessage()
		if progress == 100:
			self.successMessage()

	def putABlock(self):
		blocks = self.blocks

		if blocks != self.sizeOfCaste:
			self.blocks = blocks + 1

		self.isCastleBuilded()

	def removeABlock(self):
		blocks = self.blocks

		if blocks != 0:
			self.blocks = blocks - 1
		else:
			print('There is not nothing to destroy.')

		self.isCastleBuilded()

	def buidCastle(self):
		print(self.blocks, self.sizeOfCaste)
		if self.blocks == self.sizeOfCaste:
			return False

		random_integer = randint(0, 1)
		if random_integer == 1:
			self.putABlock()
		else:
			self.removeABlock()

		self.buidCastle()


class Idea(Worker):
	def __init__(self, sizeOfCaste=20):
		super(Worker, self).__init__(sizeOfCaste)
	def successMessage(self):
		return 'It was the delux Idea to build the castle!'
	def failureMessage(self):
		return 'I will try again!'

class Boaring(Idea):
	def __init__(self, sizeOfCaste=8):
		super(Worker, self).__init__(sizeOfCaste)
	def successMessage(self):
		return 'Yeah...I did it. I am sooo happy.'
	def failureMessage(self):
		return 'Oh...Will i be to do it again?'


a = Worker()
b = Idea()
c = Boaring()


print('c is b: %s, a is c: %s, b is a: %s.' % (c is b, a is c, b is a))

a.buidCastle()
b.buidCastle()
c.buidCastle()
