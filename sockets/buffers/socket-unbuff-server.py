from socket import *

s = socket()
s.bind(('', 60000))
s.listen(5)
print('accepting...')
conn, id = s.accept()

for i in range(3):
	print('receiving...')
	msg = conn.recv(1024)
	print(msg)