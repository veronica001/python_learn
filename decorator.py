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


func1 = sum(11,12)
func2 = mul(3,4)
if func1 == 23 and func2 == 12:
    print('测试成功')
else:
    print('测试失败')

print('--------------------------------------------------------------------------------------------')

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
def func3():
    print('test')

func3()

print('--------------------------------------------------------------------------------------------')
#log函数不能采用默认参数是因为如果采用默认参数则log是一个函数，不再是装饰器，必须有括号，而上面方法中，
# 当log有参数时它是一个函数，其中定义了一个装饰器，
# 当没有参数时它就是一个装饰器。
def log(x=''):
    if isinstance(x, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **fw):
                print('%s %s'% (x,func.__name__))
                return func(*args, **fw)
            return wrapper
        return decorator
    else:
        @functools.wraps(x)
        def wrapper(*args, **fw):
            print('call %s' % x.__name__)
            return x(*args, **fw)
        return wrapper

@log
def f1():
    print('hello f1')

@log()
def f2():
    print('hello f2')

@log('execute')
def f3():
    print('hello f3')


f1()
f2()
f3()