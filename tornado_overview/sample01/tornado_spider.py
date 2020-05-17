# -*- coding:utf-8 _*-
"""
@author: ashing
@time: 2020/5/17 11:57 上午
@mail: axingfly@gmail.com
Less is more.
"""

from urllib.parse import urljoin
from bs4 import BeautifulSoup

from tornado import gen, httpclient, ioloop, queues

base_url = "https://blog.ronething.cn"
concurrency = 3


async def get_url_links(url):
    response: httpclient.HTTPResponse = await httpclient.AsyncHTTPClient().fetch(base_url)
    html = response.body.decode()
    soup = BeautifulSoup(html)
    links = [urljoin(base_url, a.get("href")) for a in soup.find_all("a", href=True)]  # 不是 io 操作
    return links


async def main():
    seen_set = set()
    q = queues.Queue()

    async def fetch_url(current_url):
        if current_url in seen_set:
            return
        print(f"获取 {current_url}")
        seen_set.add(current_url)
        next_urls = await get_url_links(current_url)
        for new_url in next_urls:
            if new_url.startswith(base_url) and not new_url.endswith("#more"):  # 不是外链才爬取 blog #more 去除
                await q.put(new_url)  # 加入队列

    async def worker():
        # while 1:
        #     await q.get()
        async for url in q:  # async for 这个语法 需要类实现 __aiter__ magic func
            if url is None:
                return
            try:
                await fetch_url(url)
            except Exception as e:
                print("exception")
            finally:
                q.task_done()

    await q.put(base_url)  # add base url to queue
    gen.multi([worker() for _ in range(concurrency)])  # 启动三个 worker
    await q.join()  # Block until all items in the queue are processed.
    for _ in range(concurrency):  # 每个协程取得是同一个 queue
        await q.put(None)


if __name__ == '__main__':
    # base_url = "https://blgo.roenthing.cn"
    # next_url = "https://baidu.com/hello"
    # print(urljoin(base_url, next_url))
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(main)
