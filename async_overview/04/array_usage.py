# -*- coding:utf-8 _*-

__author__ = 'ronething'

# array, deque
# TODO 免费课程学习 https://www.imooc.com/learn/934 python必学模块-collections
"""
array 和 list 的一个重要区别
**array 只能存放指定类型的数据**
"""

import array

my_array = array.array('i')

my_array.append(1)
my_array.append('panda')  # TypeError: an integer is required (got type str)
