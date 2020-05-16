# -*- coding:utf-8 _*-

__author__ = 'ronething'

import contextlib


@contextlib.contextmanager
def hello():
    print("enter")
    yield  # 生成器 默认直接 yield 相当于 yield None
    print("exit")


with hello() as w:
    print(w)  # None
    print("do something")
