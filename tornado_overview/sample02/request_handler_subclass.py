# -*- coding:utf-8 _*-
"""
    created by ashing 2020/5/23 3:08 下午
    Less is more.
"""

from tornado.web import StaticFileHandler, RedirectHandler
from tornado import web, ioloop


class MainHandler(web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write("hello")

    def post(self, *args, **kwargs):
        self.write("hello")
        # self.finish("panda") # 调用 finish 会完成 response
        self.write("world")  # helloworld


settings = {
    "static_path": "/Users/ronething/PycharmProjects/python-async/tornado_overview/sample02/static",
    "static_url_prefix": "/static2/",
}

# 配置正则
url = [
    ("/", MainHandler),
    ("/2", RedirectHandler, {"url": "/"}),
    ("/static3/(.*)", StaticFileHandler,
     {"path": "/Users/ronething/PycharmProjects/python-async/tornado_overview/sample02/static"}
     )
]

if __name__ == '__main__':
    app = web.Application(url, debug=True)
    app.listen(port=8887, address="127.0.0.1")
    ioloop.IOLoop.current().start()
