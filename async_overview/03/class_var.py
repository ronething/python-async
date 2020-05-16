# -*- coding:utf-8 _*-

__author__ = 'ronething'


class A:
    aa = 1

    def __init__(self, x, y):
        """
        self 为对象 即类的实例
        """
        self.x = x
        self.y = y


a = A(2, 3)
A.aa = 11
a.aa = 100  # 相当于 self.aa = 100 实例多了一个 aa 属性
# 2 3 100
# 11
print(a.x, a.y, a.aa)  # 属性查找方式 实例变量没有找到则会查找类变量
print(A.aa)
