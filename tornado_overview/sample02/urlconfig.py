# -*- coding:utf-8 _*-
"""
@author: ashing
@time: 2020/5/19 11:53 下午
@mail: axingfly@gmai.com
Less is more.
"""

from tornado import web, ioloop
from tornado.web import URLSpec


class MainHandler(web.RequestHandler):
    # 重载 get method
    async def get(self, *args, **kwargs):
        self.write(f"hello tornado")


class PeopleIdHandler(web.RequestHandler):
    async def get(self, id, *args, **kwargs):
        self.write(f"用户 id {id}")


class PeopleNameHandler(web.RequestHandler):
    async def get(self, name, *args, **kwargs):
        self.write(f"用户姓名 {name}")


class PeopleInfoHandler(web.RequestHandler):
    async def get(self, name, id, gender, *args, **kwargs):
        self.write(f"用户 id {id}, 用户姓名 {name}, 用户性别 {gender}")


# 配置正则
url = [
    ("/", MainHandler),
    (r"/people/(\d+)/?", PeopleIdHandler),
    (r"/people/(\w+)/?", PeopleNameHandler),
    (r"/people/(\w+)/(\d+)/(\w+)/?", PeopleInfoHandler),
]

if __name__ == '__main__':
    app = web.Application(url, debug=True)
    app.listen(port=8887, address="127.0.0.1")
    ioloop.IOLoop.current().start()
