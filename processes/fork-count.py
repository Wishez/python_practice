# -*- encoding: utf-8 -*-
import os, time
def counter(count): # Вызывается в новомипроцессе
    for i in range(count):
        time.sleep(1) # имитирует работу
        print('[%s] => %s' % (os.getpid(), i))

for i in range(5):
    pid = os.fork()
    if pid != 0:
        print('Process %d spawned' % pid)
    else:
        counter(5)
        os._exit(0)

print('Main process exiting.')