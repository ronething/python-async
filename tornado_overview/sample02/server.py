# -*- coding:utf-8 _*-
"""
@author: ashing
@time: 2020/5/17 2:17 下午
@mail: axingfly@gmail.com
Less is more.
"""

from tornado import web, ioloop


class MainHandler(web.RequestHandler):
    # 重载 get method
    async def get(self, *args, **kwargs):
        self.write(f"hello tornado")


if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler),
    ], debug=True)
    app.listen(port=8887, address="127.0.0.1")
    ioloop.IOLoop.current().start()
