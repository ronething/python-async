# -*- coding:utf-8 _*-

__author__ = 'ronething'

# GIL global interpreter lock 全局解释器锁
# python 中的一个线程对应 c 语言的一个线程
# gil 使得同一个时刻只有一个线程在 cpu 上执行字节码，无法将多个线程映射到多个 cpu 上执行

# gil 会根据执行的字节码行数以及时间片释放 gil 还会在遇到 io 操作的时候主动释放
