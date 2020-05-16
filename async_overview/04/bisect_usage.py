# -*- coding:utf-8 _*-

__author__ = 'ronething'

import bisect

# 用来处理已排序的序列 用来维持已排序的序列 升序
# 二分查找

inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)
bisect.insort(inter_list, 4)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)

# bisect_right or bisect_left 查找出插入位置 可用于有些要求比较严格的排序序列
print(bisect.bisect(inter_list, 3))  # 3 相当于 bisect_right
print(bisect.bisect_left(inter_list, 3))  # 2
print(inter_list)  # [1, 2, 3, 4, 5, 6]
