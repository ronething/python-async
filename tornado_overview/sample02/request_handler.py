# -*- coding:utf-8 _*-
"""
@author: ashing
@time: 2020/5/23 1:48 下午
@mail: axingfly@gmail.com
Less is more.
"""
from tornado import web, ioloop
from tornado.routing import URLSpec
from tornado.web import RequestHandler


class MainHandler(RequestHandler):
    # def initialize(self, db):
    #     # 用于初始化 handler 类的过程
    #     self.db = db
    #     pass

    def prepare(self):
        pass

    def on_finish(self):
        pass

    def get(self, *args, **kwargs):
        data = self.get_query_argument("name")
        data2 = self.get_query_arguments("name")
        data3 = self.get_argument("name")
        data4 = self.get_arguments("name")
        self.get_body_argument("name")
        self.get_body_arguments("name")
        pass

    def post(self, *args, **kwargs):
        self.write("hello")
        # self.finish("panda") # 调用 finish 会完成 response
        self.write("world")  # helloworld


# 配置正则
url = [
    URLSpec("/", MainHandler, name="index"),
]

if __name__ == '__main__':
    app = web.Application(url, debug=True)
    app.listen(port=8887, address="127.0.0.1")
    ioloop.IOLoop.current().start()
