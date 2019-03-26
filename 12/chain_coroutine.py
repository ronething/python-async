# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-03-26 23:12 
@mail: axingfly@gmail.com

Less is more.
"""

# 协程嵌套
import asyncio


async def compute(x, y):
    print('Compute %s %s' % (x, y))
    await  asyncio.sleep(1)
    return x + y


async def print_sum(x, y):
    result = await  compute(x, y)
    print('%s + %s = %s' % (x, y, result))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()
