# -*- encoding: utf-8 -*-
from tkinter import Tk, mainloop
from form import Form 
from tkinter.messagebox import showinfo
import  os, sys, _thread 
from getfile import FTPHandler

class FtpForm(Form):
	def __init__(self):
		root = Tk()
		root.title = 'My Awesome FTP Form'
		labels = ['Server Name', 'Remote Dir', 'File Name', 'Local Dir', 'User Name?', 'Password?']
		super(FtpForm, self).__init__(labels, root)
		self.mutex = _thread.allocate_lock()
		self.threads = 0
	def transfer(self, filename, servername, remotedir, userinfo):
		try:
			self.do_transfer(filename, servername, remotedir, userinfo)
			print('%s of "%s" successful' % (self.mode, filename))
		except:
			print('%s of "%s" as failed:' % (self.mode, filename), end=' ')
			info = sys.exc_info()
			print(info[0], info[1])
		self.mutex.acquire()
		self.threads -= 1
		self.mutex.release()
	def get_value(self, label):
		return self.content[label].get()
	def onSubmit(self):
		super(FtpForm, self).onSubmit()

		localdir  = self.get_value('Local Dir')
		remotedir = self.get_value('Local Dir')
		servername = self.get_value('Local Dir')
		filename = self.get_value('Local Dir')
		username = self.get_value('Local Dir')
		password = self.get_value('Local Dir')
		userinfo = ()
		if username and password:
			userinfo = (username, password)
		if localdir:
			os.chdir(localdir)

		self.mutex.acquire()
		self.threads += 1
		self.mutex.release()

		ftpargs = (filename, servername, remotedir, userinfo,)
		_thread.start_new_thread(self.transfer, ftpargs)
		showinfo(self.title, '%s of "%s" started' % (self.mode, filename))

	def onCancel(self):
		if self.threads == 0:
			Tk().quit()
		else:
			showinfo(self.title, 'Cannot exit: %d threads running' % self.threads)

class FtpGetfileForm(FtpForm):
	title = 'My GUI for getting file'
	mode = 'Download'
	def do_transfer(self, filename, servername, remotedir, userinfo):
		handler = FTPHandler(
			servername,
			userinfo
		)

		handler.getfile(filename, remotedir)

if __name__ == '__main__':
	FtpGetfileForm()
	mainloop()

