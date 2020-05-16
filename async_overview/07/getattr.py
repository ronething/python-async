# -*- coding:utf-8 _*-

__author__ = 'ronething'


class User:
    def __init__(self, name):
        self._name = name

    def __getattr__(self, item):
        """
        可以在这里实现逻辑
        """
        return 'no find'

    def __getattribute__(self, item):
        """
        比 __getattr__ 更早被调用 尽量不重写 控制类的属性访问
        """
        pass


if __name__ == "__main__":
    user = User('panda')
    print(user.ddd)
