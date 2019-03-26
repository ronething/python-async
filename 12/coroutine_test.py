# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-03-26 21:33 
@mail: axingfly@gmail.com

Less is more.
"""

# 1. run_until_complete
import asyncio


# loop = asyncio.get_event_loop()
# loop.run_forever() # 永久 run
# loop.run_until_complete() # 可以停止

async def get_html(sleep_times):
    print('waiting')
    await asyncio.sleep(sleep_times)
    print('done after {}s'.format(sleep_times))


if __name__ == '__main__':
    task1 = get_html(2)
    task2 = get_html(3)
    task3 = get_html(3)

    tasks = [task1, task2, task3]

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print(task)  # 此时会有 4 个 除了 3 个 get_html 还有一个 wait
            print('cancel task')
            print(task.cancel())
        loop.stop()
        loop.run_forever()  # ⚠️ 此处必须 否则会抛出异常
    finally:
        loop.close()
