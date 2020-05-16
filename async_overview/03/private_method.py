# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
Java C++ 中有 private python 没有
使用 __ 声明私有属性 但其实还是可以访问到的 变为 _classname__attr
编码的一种规范 没有绝对的安全
"""

from static_class_method import Date


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        """返回年龄"""
        return 2019 - self.__birthday.year


if __name__ == "__main__":
    user = User(Date(1999, 10, 1))
    # 'User' object has no attribute '__birthday'
    # print(user.__birthday)
    print(user._User__birthday)
    print(user.get_age())