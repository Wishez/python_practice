import time, sys

def now():
	return time.ctime(time.time())

for i in range(5):
	print(now())
	sys.stdout.write('\nspam')
	time.sleep(2)