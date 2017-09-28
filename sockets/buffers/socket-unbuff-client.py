from socket import *
import time

s = socket()
s.connect(('194.67.218.82', 60000))
file = s.makefile('w', 1)
print('sending data1')
file.write('spam\n')
time.sleep(2)
file.flush()

print('sending data2')
print('eggs', file)
time.sleep(2)
file.flush()

print('sending data3')
# This string will be accepted first if 
# priveous cases won't be flushed.
s.send(b'ham\n') 
time.sleep(5)

# C:\cygwin64\scripts\python_practice\sockets\buffers>
# python socket-unbuf-client.py