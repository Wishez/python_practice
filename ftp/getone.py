import os, sys
from getpass import getpass, getuser # Проверить документацию, на счёт этой загаточной функции, которая позволяет подключиться анонимно к серверу.
from ftplib import FTP

nonpassive = False
filename = 'richard.jpg'
dirname = '/playing'
sitename = '194.67.218.82'
print(getuser())
userinfo = (input('Login: '), getpass('Password: ')) 
if len(sys.argv) > 1: filename = sys.argv[1]

print('Connecting...')
connection = FTP(sitename) # Создаю FTP соединение - 2 сокета на 21 и 20 портах, первый из которых принимает управляющие команды, а второй предаёт бинарные данные.
print(userinfo)
connection.login(*userinfo) # Неопределённое количество позиционных аргументов пердаю в функцию, требующая данные пользователя.
connection.cwd(dirname) # Переходит  в указанную директорию на сервере. cwd ー Curren Work Directory.
if nonpassive: # Использует активный режим, если этого требует сервер.
	connection.set_pasv(False)

print('Downloading...')
localfile = open(filename, 'wb') # Создаётся файл, в который будут копироваться все данные из запрошенного файла.
connection.retrbinary('RETR ' + filename, localfile.write, 1024) # Не понимаю, что не делает первый аргумент, но очевидно, что сама функция записывает в файл данные.
connection.quit()
localfile.close() # Файл записался, можно закрывать

if input('Open file?') in ['Y', 'y']:
	from ftp.playfile import playfile
	playfile(filename)

