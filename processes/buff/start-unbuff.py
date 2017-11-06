import os, sys

for line in os.popen('python -u unbuff-writer.py'):
	print(line, end='') 