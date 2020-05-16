# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
自省是通过一定的机制查询到对象的内部结构
"""


class Person:
    name = "user"


class Student(Person):
    def __init__(self, school):
        self.school = school


if __name__ == "__main__":
    user = Student('SCAU')

    # 通过 __dict__ 查询属性
    print(user.__dict__)
    user.__dict__['add_attr'] = 'by_dict'
    print(user.add_attr)  # by_dict
    print(user.__dict__)  # {'school': 'SCAU', 'add_attr': 'by_dict'}

    # dir 很强大
    print(dir(user))

    a = [1, 2]
    # print(a.__dict__) AttributeError: 'list' object has no attribute '__dict__'
    print(dir(a))
