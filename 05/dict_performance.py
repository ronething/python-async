# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
dict 查找的性能远远大于 list
在 list 中随着 list 数据的增大 查找时间会增大
在 dict 中查找元素 dict 数据的增大不影响查找时间

dict 中的 key 或者 set 的值 都必须是可以 hash 的
不可变对象都是可 hash 的 例如 str frozenset tuple 自己实现的类 重写 __hash__
dict 内存花销大 但是查询速度快
dict 的存储顺序和元素添加顺序有关
添加数据有可能改变已有数据的顺序
"""
