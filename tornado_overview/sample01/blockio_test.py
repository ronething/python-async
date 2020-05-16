# -*- coding:utf-8 _*-
"""
@author: ashing
@time: 2020/5/16 11:00 下午
@mail: axingfly@gmail.com
Less is more.
"""


# 阻塞 io
# import requests
# html = requests.get("http://www.baidu.com").text
# 1、三次握手建立连接
# 2、等待服务器相应

# 如何通过 socket 直接获取 html
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "www.baidu.com"
client.connect((host, 80)) # 阻塞 io
client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format("/", host).encode("utf8"))

data = b""
while 1:
    d = client.recv(1024)
    if d:
        data += d
    else:
        break

data = data.decode("utf8")

if __name__ == '__main__':
    # print(html)
    print(data)


