# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-02 19:17 
@mail: axingfly@gmail.com

Less is more.
"""

# asyncio 没有提供 http 协议的接口
# aiohttp 可以当成异步的 request

import asyncio

import socket
from urllib.parse import urlparse


async def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    # print(host, path)
    if path == "":
        path = "/"

    # 建立socket连接
    reader, writer = await asyncio.open_connection(host, 80)

    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(
        path, host).encode("utf8"))
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # # client.setblocking(False)
    # client.connect((host, 80))  # 阻塞不会消耗cpu

    data = b''
    async for raw_line in reader:
        data += raw_line

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    # print(html_data)
    return html_data


async def main(loop):
    tasks = []
    for url in range(20):
        url = 'http://shop.projectsedu.com/goods/{}/'.format(url)
        # tasks.append(get_url(url))
        tasks.append(asyncio.ensure_future(get_url(url)))
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)


if __name__ == '__main__':
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    # for task in tasks:
    #     print(task.result())
    print('use time:{}'.format(time.time() - start_time))
