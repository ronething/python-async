# -*- coding:utf-8 _*-
"""
@author: ashing
@time: 2020/5/23 1:24 下午
@mail: axingfly@gmail.com
Less is more.
"""

from tornado import web, ioloop
from tornado.options import define, options, parse_command_line

# define 定义一些可以通过命令行/文件传递的参数以及类型
define('port', default=8008, help='run on the given port', type=int)
define('debug', default=True, help='', type=bool)

# 全局唯一
# options.parse_command_line() 在命令行中传递
options.parse_config_file('./conf.cfg')


class PeopleIdHandler(web.RequestHandler):

    async def get(self, id, *args, **kwargs):
        self.write(f"用户 id {id}")


# 配置正则
url = [
    (r"/people/(\d+)/?", PeopleIdHandler),
]

if __name__ == '__main__':
    app = web.Application(url, debug=options.debug)
    app.listen(port=options.port, address="127.0.0.1")
    ioloop.IOLoop.current().start()
