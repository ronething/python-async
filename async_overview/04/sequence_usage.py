# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
容器序列 list tuple deque
扁平序列 str bytes bytearray array.array
---
可变序列 list deque bytearray array
不可变序列 str tuple bytes
"""
"""
+
+= 内部实现调用了 extend
"""
a = [1, 2]
b = a + [3, 4]
print(b)
# c = a + (3,4) can only concatenate list (not "tuple") to list
a += (3, 4)
print(a)
"""
append extend
"""
a.append([1, 2])
print(a)  # [1, 2, 3, 4, [1, 2]]
a.extend([1, 2])
print(a)  # [1, 2, 3, 4, [1, 2], 1, 2]
