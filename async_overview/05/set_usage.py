# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
set 集合 无序集合
frozenset 不可变集合
"""

a = set('abcdd')
print(a)
a.add('e')
print(a)

# set 添加数据

c = set('asfd')
a.update(c)
print(a)  # {'a', 'f', 'b', 'e', 's', 'c', 'd'}

d = a.difference(c)  # 相当于 a - c
print(d)  # {'b', 'c', 'e'} 存在 a 不存在 c
e = a & c
print(e)  # {'a', 'f', 's', 'd'}
f = a | c
print(f)  # {'a', 'b', 's', 'd', 'e', 'c', 'f'}

res = True if 'a' in a else False
print(res)

print(c.issubset(a))  # Report whether another set contains this set. 此时 a 包含了 c

b = frozenset('abcdd')  # ⚠️可以作为 dict 的 key
print(b)
b.add('c')  # AttributeError: 'frozenset' object has no attribute 'add'
