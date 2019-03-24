# -*- coding:utf-8 _*-

__author__ = 'ronething'

# 函数中只要有 yield 关键字就是生成器函数


# 惰性求值，延迟求值提供可能
def gen_func():
    yield 1
    yield 2
    yield 3


def re_func():
    return 1


def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


for i in gen_fib(10):
    print(i)

if __name__ == "__main__":
    # gen 为 生成器对象 python 编译字节码的时候就生成了
    gen = gen_func()
    re = re_func()
    pass
