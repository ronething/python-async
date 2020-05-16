# -*- coding:utf-8 _*-

__author__ = 'ronething'

# 垃圾回收采用引用计数

a = object()  # 此时指向 object() 的计数为 1
b = a  # 此时指向 object() 的计数为 2
del a  # 此时指向 object() 的计数为 1
print(b)  # <object object at 0x10167d0c0>
print(a)  # NameError: name 'a' is not defined
