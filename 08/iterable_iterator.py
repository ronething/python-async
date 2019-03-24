# -*- coding:utf-8 _*-

__author__ = 'ronething'

from collections.abc import Iterator


class Company:
    def __init__(self, user_list):
        self.user_list = user_list

    def __iter__(self):
        return MyIterator(self.user_list)

    # def __getitem__(self, item):
    #     return self.user_list[item]


class MyIterator(Iterator):
    """迭代器不支持切片"""

    def __init__(self, user_list):
        self.user_list = user_list
        self.index = 0

    def __next__(self):
        """真正返回迭代值的逻辑"""
        try:
            word = self.user_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == "__main__":
    company = Company(user_list=['panda', 'xzx', 'ronething'])

    """相当于 for 遍历"""
    # iter_company = iter(company)
    # while True:
    #     try:
    #         print(next(iter_company))
    #     except StopIteration:
    #         break
        
    for item in company:
        print(item)