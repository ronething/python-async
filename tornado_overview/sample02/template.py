# -*- coding:utf-8 _*-
"""
    created by ashing 2020/5/24 12:47 上午
    Less is more.
"""

from tornado.web import template
from tornado import web, ioloop


class MainHandler(web.RequestHandler):
    async def get(self, *args, **kwargs):
        word = "hello panda"
        # t = template.Template("<h3>{{ word }}</h3>")
        # loader = template.Loader("/Users/ronething/PycharmProjects/python-async/tornado_overview/sample02/templates")
        # self.finish(loader.load("hello.html").generate(word=word))
        self.render("hello.html", word=word)
        # self.render_string()


settings = {
    "template_path": "templates",
}

url = [
    ("/", MainHandler)
]

if __name__ == '__main__':
    app = web.Application(url, debug=True, **settings)
    app.listen(port=8887, address="127.0.0.1")
    ioloop.IOLoop.current().start()
