# -*- encoding: utf-8 -*-
from ftplib import FTP
from os.path import exists

class FTPHandler():
	def __init__(
		self,
		site, 
		user=(), 
		*args, 
		verbose=True, 
		refetch=True
	):
		self.site = site
		self.user = user
		self.verbose = verbose
		self.refetch = refetch

	def say(self, message):
		if self.verbose: print(message)
	def getfile(self, file, directory): 
		self.say(self.user)
		file = file
		verbose = self.verbose

		if exists(file) and not self.refetch:
			self.say('File %s already fetched.' % file)
		else:
			self.say('Downloading the file %s...' % file)
			local = open(file, 'wb')
			try:
				# My main object for creating connection with my server.
				remote = FTP(self.site)
				# Simple user connect.
				remote.login(*self.user)
				# Change working dir on the server.
				remote.cwd(directory)
				# First argument is GET the like, second is function wich will be write data, 
				# and third is the limit of received data in binary vector.
				remote.retrbinary('RETR ' + file, local.write, 1024) 
				self.say(remote)
				remote.quit() # Close the connection.
			finally:
				# Anyway, i am going to close the file.
				local.close()
			self.say('We got it!')
	def putfile(self, file, directory):
		pushed_file = open(file, 'rb')

		if exists(file):
			remote = FTP(self.site)
			remote.login(*self.user)
			remote.cwd(directory)
			remote.storebinary('STORE ' + file, pushed_file, 1024)
			remote.quit()
			pushed_file.close()
			self.say('Uploaded %s.' % file)
		else:
			self.say('There is no such file in %s.' % file)


if __name__ == '__main__':
	from getpass import getpass

	login = input('Login: ')
	password = getpass('Password: ')
	# login = 'root'
	# password = 'Shiningfinger198237645'
	handler = FTPHandler(
		'194.67.216.135',
		(login, password,)
	)

	handler.getfile('cat.jpg', '/test')
	handler.putfile('img/city.png', '/test')
	

