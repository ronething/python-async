# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-03 01:00 
@mail: axingfly@gmail.com

Less is more.
"""

# asyncio 爬虫、去重、入库

import re
import asyncio
import aiohttp

import aiomysql

from pyquery import PyQuery

stopping = False
start_url = 'http://www.jobbole.com/'
waiting_urls = []
seen_urls = set()

sem = asyncio.Semaphore(1)


async def fetch(url, session):
    async with sem:
        await asyncio.sleep(5)
        try:
            async with session.get(url) as resp:
                print('URL status ', resp.status)
                if resp.status in [200, 201]:
                    data = await resp.text()
                    return data
        except Exception as e:
            print(e)


def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items('a'):
        url = link.attr('href')
        if url and url.startswith('http') and url not in seen_urls:
            urls.append(url)
            waiting_urls.append(url)
    return urls


async def init_urls(url, session):
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)


async def article_handler(url, session, pool):
    # 获取文章详情
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq('title').text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            insert_sql = "insert into article_title(title) values ('{}')".format(title)
            await cur.execute(insert_sql)


async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waiting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            url = waiting_urls.pop()
            print('start get url:{}'.format(url))
            if re.match('http://blog.jobbole.com/\d+/', url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url, session, pool))
                    await asyncio.sleep(3)
            else:
                if url not in seen_urls:
                    asyncio.ensure_future(init_urls(url, session))


async def core(loop):
    # 等待 mysql 连接建立好
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='root',
                                      db='article_spider', loop=loop,
                                      charset='utf8mb4', autocommit=True)
    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_urls(html)
    asyncio.ensure_future(consumer(pool))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(core(loop))
    loop.run_forever()
