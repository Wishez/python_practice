# -*- encoding: utf-8 -*- 
""" Взаимодействие между программами может происходить через
	двунаправленные каналы, а точнее через два внутренних канала канала - внешний канал
	со своими потокоми ввода и вывода, относящиеся к системным каналам, а
	также внутренние каналы, создающиеся внутри программы. 
	Что я до сих пор не понимаю: Почему поток ввода - это чтение данных, а
	поток вывода - это запись данных? Попытаюсь понять, но пока что приму это как
	факт.
"""

import sys, os

# program - это интерпертатор python, который будет браться  из
# системного пути.
# args - аргументы, которые будут передоваться в командную строку 
def spawn(prog, *args):
	# Дескрипторы голбального ввода и вывода
	# fileno - функция, открывающая дескриптор файла.
	# Потоки ввода и ввода - это псведо файлы имеющие дескриптор. 
	stdinFd = sys.stdin.fileno()
	stdoutFd = sys.stdout.fileno()
	# Потоки на запись дочерним процессом и чтение родительским.
	parentStdin, childStdout = os.pipe()
	# Наоборот.
	childStdin, parentStdout = os.pipe()
	# Создаётся поток ветвления.
	# Первый созданый процесс - родительски.
	# Второй созданый процесс - копия родительского процесса.
	pid = os.fork()
	# Если родительский процесс
	print(pid)

	if pid:
		print('Parent')
		# Закрываются дочерние потоки/дескрипторы вывода и ввода
		os.close(childStdin)
		os.close(childStdout)
		# Дескрипторы канала родительского процесса копируются в 
		# дескрипторы глобального канала
		os.dup2(parentStdin, stdinFd) 
		os.dup2(parentStdout, stdoutFd) 
	else:
		print('<Child></Child>')
		os.close(parentStdin)	
		os.close(parentStdout)
		os.dup2(childStdin, stdinFd)
		os.dup2(childStdout, stdoutFd)
		args = (prog,) + args
		# Запускается новая программа.
		os.execvp(prog, args) 
		assert False, 'execvp не запустилась!' 


if __name__ == '__main__':
	mypid = os.getpid()
	spawn('python', '-u', 'pipes-testchild.py', 'spam')



	print('Родительский процесс передаёт первый привет и свой id', mypid) 
	# вытолкнуть буфер stdio для execvp
	# sys.stdout.flush()
	reply = input() 
	sys.stderr.write('Parent got: "%s"\n' % reply)

	print('Родительский процесс передаёт второй привет и свой id', mypid) 
	# sys.stdout.flush()
	reply = sys.stdin.readline()
	sys.stderr.write('Parent got: "%s"\n' % reply[:-1])

