# -*- encoding: utf-8 -*-
from socket import *

myHost = ''
myPort = 50007


sockobj = socket(AF_INET, SOCK_STREAM)  # Объект сокета TCP
sockobj.bind((myHost, myPort))          # Привзяка объекта сокета к Адресу и ПОрту сервера
sockobj.listen(5)                       # Не более 5 ожидающих запросов от сервера

while True:
    connection, address = sockobj.accept()
    print('Server connected by', address)

    while True:
        data = connection.recv(1024) # Читаем строку из сокета
        if not data: break
        connection.send(b'Echo=>' + data)
    connection.close()