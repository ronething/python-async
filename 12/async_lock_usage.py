# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-02 20:46 
@mail: axingfly@gmail.com

Less is more.
"""

from asyncio import Lock, Queue

# 有时需要同步 queue 用来通信
cache = {}
lock = Lock()

queue = Queue()
await queue.get()


async def get_stuff(url):
    # await lock.acquire()  # acquire 是一个协程
    # if url in cache:
    #     return cache[url]
    # stuff = await aiohttp.request('GET', url)
    # cache[url] = stuff
    # lock.release()  # release 普通函数
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff


async def parse_stuff():
    stuff = await get_stuff(url)


async def use_stuff():
    stuff = await get_stuff(url)
