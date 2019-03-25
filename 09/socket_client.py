# -*- coding:utf-8 _*-

__author__ = 'ronething'

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 7070))

while True:
    re_data = input()
    client.send(re_data.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))
