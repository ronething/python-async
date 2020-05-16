# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-02 20:38 
@mail: axingfly@gmail.com

Less is more.
"""

import asyncio

total = 0


async def add():
    global total
    for i in range(1000000):
        total += 1


async def desc():
    global total
    for i in range(1000000):
        total -= 1


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [add(), desc()]
    loop.run_until_complete(asyncio.wait(tasks))
    print(total) # 单线程 不需要锁
