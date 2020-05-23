# -*- coding:utf-8 _*-
"""
@author: ashing
@time: 2020/5/19 11:53 下午
@mail: axingfly@gmai.com
Less is more.
"""

import tornado
from tornado import web, ioloop
from tornado.web import URLSpec


class MainHandler(web.RequestHandler):
    # 重载 get method
    async def get(self, *args, **kwargs):
        self.write(f"hello tornado")


class PeopleIdHandler(web.RequestHandler):
    def initialize(self, name):  # init hook
        self.db_name = name

    async def get(self, id, *args, **kwargs):
        self.write(f"用户 id {id}")
        # self.write(self.reverse_url("people_name", "panda"))
        # self.redirect(self.reverse_url("people_name", "panda"))


class PeopleNameHandler(web.RequestHandler):
    async def get(self, name, *args, **kwargs):
        self.write(f"用户姓名 {name}")


class PeopleInfoHandler(web.RequestHandler):
    async def get(self, name, id, gender, *args, **kwargs):
        self.write(f"用户 id {id}, 用户姓名 {name}, 用户性别 {gender}")


people_db = {
    "name": "people"
}

# 配置正则
url = [
    URLSpec("/", MainHandler, name="index"),
    URLSpec(r"/people/(\d+)/?", PeopleIdHandler, kwargs=people_db, name="people_id"),
    URLSpec(r"/people/(\w+)/?", PeopleNameHandler, name="people_name"),
    URLSpec(r"/people/(?P<name>\w+)/(?P<id>\d+)/(?P<gender>\w+)/?", PeopleInfoHandler, name="people_info"),
]

if __name__ == '__main__':
    app = web.Application(url, debug=True)
    app.listen(port=8887, address="127.0.0.1")
    ioloop.IOLoop.current().start()
