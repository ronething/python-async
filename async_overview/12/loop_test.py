# -*- coding:utf-8 _*-

__author__ = 'ronething'

import asyncio
import time


async def get_html(url):
    print('start get url')
    await asyncio.sleep(2)  # 不可以使用同步阻塞的方法 time.sleep(2) 来操作
    print('end get url')


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # tasks = [get_html('https://blgo.ronething.cn') for i in range(10)]
    # run_until_complete 相当于线程的 join 阻塞

    # wait 和 gather 的区别
    # gather 更加 high-level 可以分组 可以取消任务
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.run_until_complete(asyncio.gather(*tasks))
    group1 = [get_html('https://blgo.ronething.cn') for i in range(10)]
    group2 = [get_html('https://blgo.ronething.cn') for i in range(10)]
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    group2.cancel()
    loop.run_until_complete(asyncio.gather(group1, group2))
    print(time.time() - start_time)
