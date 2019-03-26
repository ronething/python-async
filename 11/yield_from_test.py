# -*- coding:utf-8 _*-

__author__ = 'ronething'


def g1(iterable):
    yield iterable

def d1(iterable):
    x = yield
    yield from iterable
    yield 1
    yield 2

def g2(iterable):
    yield from d1(iterable)


if __name__ == "__main__":
    # print(type(next(g1([1, 2, 3]))))
    # for i in g1([1, 2, 3]):
    #     print(i)
    # for i in g2([1, 2, 3]):
    #     print(i)
    g = g2([1,2,3])
    g.send(None)
    for i in g:
        print(i)