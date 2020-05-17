# -*- coding:utf-8 _*-
"""
@author: ashing
@time: 2020/5/16 11:00 下午
@mail: axingfly@gmail.com
Less is more.
"""

import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过 socket 请求 html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立 socket 连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))  # 阻塞不会消耗 cpu
    except BlockingIOError as e:
        pass

    # 不停的询问连接是否建立好， 需要 while 循环不停的去检查状态
    # 做计算任务或者再次发起其他的连接请求

    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as e:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()


if __name__ == '__main__':
    get_url("https://www.baidu.com")
