# -*- encoding: utf-8 -*-
import os, getpass, sys
from urllib.request import urlopen # веб инструмент на основе сокетов
filename = 'cat.jpg'
print(sys.argv)
if len(sys.argv) > 1:
	filename = sys.argv[1]

password = getpass.getpass('Pswd?')

remoteaddr = 'ftp://root:%s@web-renome.ru/%s;type=i' % (password, filename)
print('Downloading', remoteaddr)

# urllib.request.urlretreive(remoteaddr, filename)

remotefile = urlopen(remoteaddr)
localfile = open(filename, 'wb')
localfile.write(remotefile.read())
localfile.close()
remotefile.close()