# -*- encoding: utf-8 -*- 

import os, time, sys
mypid = os.getpid()

parentpid = os.getppid()
sys.stderr.write('Ребёнок %d родителя %d получил аргументы: "%s"\n' % 
	(mypid, parentpid, sys.argv[1]))

for i in range(2):
	# Родительски процесс приостанавливается.
	time.sleep(3) 
	# stdin связан с каналом ввода родительского процесса,
	# то есть из stdout, из буфера вывода будут поступать данные
	# для их чтения дочерним процессом.
	recv = input() 

	time.sleep(3)
	send = 'Дочерний процесс %d получил: [%s]' % (mypid, recv)
	print(send)
	# Гарантия, что данные будут вытолкнуты из буфера ввода дочернего 
	# процесса.
	# sys.stdout.flush()