# -*- coding:utf-8 _*-

__author__ = 'ronething'
"""
魔法函数 双下划线开头 双下划线结束
用于增强类的特性 不是某个类独有
__init__ __getitem__ .etc
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        # print(item)
        return self.employee[item]

    def __len__(self):
        # return 10
        return len(self.employee)


company = Company(['Panda', 'Ronething'])

emploee = company.employee
# for i in emploee:
#     print(i)
# for em in company:
#     print(em)
print(len(company))