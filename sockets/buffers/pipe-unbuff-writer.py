import sys, time
for i in range(5):
	print(time.ctime(time.time()))
	sys.stdout.write('spam\n')
	# sys.stdout.flush()
	time.sleep(2)