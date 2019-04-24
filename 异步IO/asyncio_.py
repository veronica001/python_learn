#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中
执行，就实现了异步IO。
'''
import threading
import asyncio

# @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
@asyncio.coroutine
def hello():
    print('hello world! (%s)' % threading.currentThread())
    # 异步调用asyncio.sleep(1)
    # 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
    r = yield from asyncio.sleep(1)
    print('hello again! (%s)' % threading.currentThread())

# 获取eventloop
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()