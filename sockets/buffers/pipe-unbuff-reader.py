import os, sys
# User -u option for setting unbuffered mode.
for line in os.popen('python pipe-unbuff-writer.py'):
	print(line, end='')
	# If here to use sys.stdout.flush(), text doesn't show up in a console.