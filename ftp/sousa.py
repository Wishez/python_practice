from getfile import FTPHandler
from getpass import getpass

if __name__ == '__main__':
	file = 'sousa.au'
	site = 'ftp.rmi.net'
	dir = '.'
	user = ('lutz', getpass('Pswd?'),) 
	handler = FTPHandler(
		site,
		user
	)

	handler.getfile(file, dir)