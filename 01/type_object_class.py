# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
type object class 的关系
"""

# type->int->1

type(1)  # int
type(int)  # type

# type->class->obj


class Student:
    pass


stu = Student()

type(stu)  # __main__.Student

type(Student)  # type

# object 是最顶层基类
# type 即是一个类 同时也是一个对象

object.__bases__  # ()
type.__bases__  # (object,)
type(object)  # type
