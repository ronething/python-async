# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
with 上下文管理器
"""


def exe_try():
    try:
        print('try')
        raise KeyError
        return 1
    except KeyError:
        print('key error')
        return 2  # 此时把 2 压入栈中
    else:
        # 没有抛出异常的时候才执行
        print('else')
        return 3
    finally:
        # 无论如何运行
        print('finally')
        return 4  # 此时把


print(exe_try())  # 4


# 上下文管理器
class Simple:
    def __enter__(self):
        # 获取资源
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print('exit')

    def do_something(self):
        return 'do something'


with Simple() as sample:
    print(sample.do_something())
