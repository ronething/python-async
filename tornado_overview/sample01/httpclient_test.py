# -*- coding:utf-8 _*-
"""
@author: ashing
@time: 2020/5/17 11:03 上午
@mail: axingfly@gmail.com
Less is more.
"""

from tornado import httpclient, ioloop


# def main():
#     http_client = httpclient.HTTPClient()
#     try:
#         response = http_client.fetch("https://www.tornadoweb.org/en/branch5.1/httpclient.html")
#         print(response.body.decode())
#     except httpclient.HTTPError as e:
#         # HTTPError is raised for non-200 responses; the response
#         # can be found in e.response.
#         print("Error: " + str(e))
#     except Exception as e:
#         # Other errors are possible, such as IOError.
#         print("Error: " + str(e))
#     http_client.close()


async def f():
    http_client = httpclient.AsyncHTTPClient()
    try:
        response = await http_client.fetch("https://blog.ronething.cn")
    except Exception as e:
        print("Error: %s" % e)
    else:
        print(response.body.decode())


if __name__ == '__main__':
    # main()

    # import asyncio
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(f())

    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(f)
