# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-03 16:29 
@mail: axingfly@gmail.com

Less is more.
"""

import asyncio


def callback(sleep_times):
    print('sleep {} success'.format(sleep_times))


def stop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # call_soon 不是立即执行 而是等待下一个事件循环则执行
    # loop.call_soon(callback, 3)

    # call_later
    # loop.call_later(2, callback, 1)
    # loop.call_later(1, callback, 3)
    # loop.call_later(3, callback, 2)
    # 3 1 2 根据 delay 时间来执行顺序

    # call_at
    now = loop.time()  # 内部时钟时间
    loop.call_at(now + 1, callback, 1)
    loop.call_at(now + 3, callback, 3)
    loop.call_at(now + 2, callback, 2)

    # loop.call_soon(stop, loop)
    loop.run_forever()
