#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
用错误码来表示是否出错十分不便,所以高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。

try
    当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误
    处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
https://docs.python.org/3/library/exceptions.html#exception-hierarchy


'''

'''
有return的情况下try catch finally的执行顺序
结论：
1、不管有没有出现异常，finally块中代码都会执行；
2、当try和catch中有return时，finally仍然会执行；
3、finally是在return后面的表达式运算后执行的（此时并没有返回运算后的值，而是先把要返回的值保存起来，
    不管finally中的代码怎么样，返回的值都不会改变，任然是之前保存的值），所以函数返回值是在finally执行前确定的；
4、finally中最好不要包含return，否则程序会提前退出，返回值不是try或catch中保存的返回值。
'''

try:
    print('try...')
    r = 10 / 0
    print('result : %d' % r)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally')
print('END')

'''
使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出
错了，这时，只要main()捕获到了，就可以处理：
只要在合适的层次去捕获错误就可以了
'''
def foo(s):
    return 10 / int(s)

def bar(s):
    foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
        # logging.exception(e)
    finally:
        print('finally...')

main()

'''
 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。 
 Python内置的logging模块可以非常容易地记录错误信息
 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内
置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
用raise语句抛出一个错误的实例
尽量使用Python内置的错误类型

raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
 '''
class FooError(ValueError):
    pass
def foo1(s):
    n = int(s)
    if n == 0:
        # raise FooError('invalid value: %s' % s)
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar1():
    try:
        foo1('0')
    except ValueError as e:
        print('ValueError')
        raise

# bar1()

# 练习 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
