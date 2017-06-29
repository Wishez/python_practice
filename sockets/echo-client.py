import sys
from socket import *
serverHost = 'localhost'
serverPort = 50007

message = [b'It\'s message sending to a server']

if len(sys.argv) > 1:
    serverHost = sys.argv[1]# Сервер в аргументе 1 командой строки
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

    sockobj = socket(AF_INET, SOCK_STREAM) # Объект сокета TCP/IP
    sockobj.connect((serverHost, serverPort))

    for line in message:
        sockobj.send(line) # Послать серверу строчку
        data = sockobj.recv(1024) # Получить строку от сервера
        print('Client received:', data)

    sockobj.close()