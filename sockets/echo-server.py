# -*- encoding: utf-8 -*-
import sys
from socket import *
import pickle
myHost = ''
myPort = 50007


sockobj = socket(AF_INET, SOCK_STREAM)  # Объект сокета TCP
sockobj.bind((myHost, myPort))          # Привзяка объекта сокета к Адресу и ПОрту сервера
sockobj.listen(5)                       # Не более 5 ожидающих запросов от сервера

while True:
    connection, address = sockobj.accept()
    print('Server connected by', address)
    obj = {
        'firstReceiveData': '',
        'fullChangedData': 'You sent - ',
        'lengthData': 0
    }
    while True:
        data = connection.recv(1024) # Читаем строку из сокета
        data = str(data)
        if not data:break
        if obj['lengthData'] == 0:
            obj['firstReceiveData'] = data
        obj['fullChangedData'] += data
        obj['lengthData'] += 1

    connection.send(pickle.dumps(obj))
    connection.close()

#cd dev/python_practice/sockets
# python server-