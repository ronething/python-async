# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-03-26 20:32 
@mail: axingfly@gmail.com

Less is more.
"""

import asyncio
import time

# partial 将一个函数包装成另一个函数
from functools import partial


async def get_html(url):
    print('start get url')
    await asyncio.sleep(2)  # 不可以使用同步阻塞的方法 time.sleep(2) 来操作
    print('end get url')
    return 'panda'


def callback(url, future):
    print(url)
    # print(future.result())
    print('callback done')


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # run_until_complete 相当于线程的 join 阻塞

    # 1. 通过 asyncio.ensure_future
    # get_future = asyncio.ensure_future(get_html('https://blog.ronething.cn'))
    # loop.run_until_complete(get_future)

    # 2. 通过 loop.create_task
    task = loop.create_task(get_html('https://blog.ronething.cn'))
    # 执行完成的回调
    # task.add_done_callback(callback)
    task.add_done_callback(partial(callback, 'https://blog.ronething.cn'))
    loop.run_until_complete(task)

    # 获取协程的返回值
    # print(get_future.result())
    # print(task.result())

    print(time.time() - start_time)
