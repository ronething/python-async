# -*- coding:utf-8 _*-

__author__ = 'ronething'

import time
import os

print('xixi')
pid = os.fork()
print('pid is {}'.format(pid))

if pid == 0:
    print('子进程{} 父进程{}'.format(os.getpid(), os.getppid()))
else:
    print('父进程{}'.format(pid))

time.sleep(2)  # 没有这个 sleep 子进程无法退出
