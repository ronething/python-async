# -*- coding:utf-8 _*-
"""
    created by ashing 2020/5/24 12:47 上午
    Less is more.
"""

from tornado.web import template
from tornado import web, ioloop


class MainHandler(web.RequestHandler):
    def calc_total(self, price, nums):
        return price * nums

    async def get(self, *args, **kwargs):
        word = "hello panda"
        # t = template.Template("<h3>{{ word }}</h3>")
        # loader = template.Loader("/Users/ronething/PycharmProjects/python-async/tornado_overview/sample02/templates")
        # self.finish(loader.load("hello.html").generate(word=word))
        # self.render("hello.html", word=word)
        # self.render_string()
        orders = [
            {
                "name": "小米 T 恤 忍者米兔双截棍 军绿 XXL",
                "image": "http://i1.mifile.cn/a1/T11lLgB5YT1RXrhCrK!40x40.jpg",
                "price": 39,
                "nums": 3
            },

            {
                "name": "招财猫米兔 白色",
                "image": "http://i1.mifile.cn/a1/T14BLvBKJT1RXrhCrK!40x40.jpg",
                "price": 49,
                "nums": 2
            },

            {
                "name": "小米圆领纯色 T 恤 男款 红色 XXL",
                "image": "http://i1.mifile.cn/a1/T1rrDgB4DT1RXrhCrK!40x40.jpg",
                "price": 59,
                "nums": 1
            }
        ]
        # self.render("index.html", orders=orders, calc_total=self.calc_total)
        self.render("index.html", orders=orders)


settings = {
    "static_path": "/Users/ronething/PycharmProjects/python-async/tornado_overview/sample02/static",
    "static_url_prefix": "/static/",
    "template_path": "templates",
}

url = [
    ("/", MainHandler)
]

if __name__ == '__main__':
    app = web.Application(url, debug=True, **settings)
    app.listen(port=8887, address="127.0.0.1")
    ioloop.IOLoop.current().start()
