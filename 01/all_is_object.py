# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
python 中一切皆是对象
函数和类也是对象，属于 python 的一等公民
"""


def ask(name='ronething'):
    print(name)


class Person:
    def __init__(self):
        print('ronething')


def decorator_func():
    print("decorator_func")
    return ask


my_ask = decorator_func()
my_ask('xzx')

# obj_list = []
# obj_list.extend([ask, Person])

# for item in obj_list:
#     print(item())

# my_func = ask
# my_func('panda')

# my_class = Person
# my_class()
