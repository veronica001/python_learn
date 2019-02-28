#! /usr/bin/env python
# -*- coding: utf-8 -*-
#  返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('%s excute %s s'% ( fn.__name__, 10.24 ))
        return fn(*args, **kw)
    return wrapper

@metric
def sum(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def mul(x, y):
    time.sleep(0.1234)
    return x * y


f1 = sum(11,12)
f2 = mul(3,4)
if f1 == 23 and f2 == 12:
    print('测试成功')
else:
    print('测试失败')


# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def decorator(func):
    functools.wraps(func)
    def wrapper(*args, **fw):
        print('begin call')
        ret = func(*args, **fw)
        print('end call')
        return ret
    return wrapper

@decorator
def func():
    print('test')


def log(x):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **fw):
            print('%s'% (x))
            return func(*args, **fw)
        return wrapper
    return decorator

@log('excute')
def f1():
    print('haha')

# @log
# def f2():
#     print('haha1')

f1()
# f2()