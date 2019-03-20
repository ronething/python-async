# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
实现一个可以支持 slice 切片操作的 class
不可修改序列
"""

import numbers


class Group:
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(
                group_name=self.group_name,
                company_name=self.company_name,
                staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(
                group_name=self.group_name,
                company_name=self.company_name,
                staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


staffs = ['panda', 'xzx', 'ronething']
group = Group(company_name='ahh..', group_name='user', staffs=staffs)
print(group[:2].staffs)
print(group[2].staffs)
print(len(group))
if 'panda' in group:
    print('yes')
for i in group:
    print(i)
reversed(group)
for i in group:
    print(i)
