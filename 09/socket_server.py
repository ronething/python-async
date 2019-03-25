# -*- coding:utf-8 _*-

__author__ = 'ronething'

import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0', 7070))
server.listen()


def handle_sock(sock, addr):
    # 获取从客户端发送的数据
    # 一次获取 1k 的数据
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        re_data = input()
        sock.send(re_data.encode('utf-8'))


while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()
