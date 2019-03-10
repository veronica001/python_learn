#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# 日期：2019-03-10 17:03
# 工具：PyCharm
# Python版本：3.6.3

# 对函数fact(n)编写doctest并执行：

def fact(n):
    '''
    fact(n): 1*2*...*n

    >>> fact(1)
    1
    >>> fact(5)
    120
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: -1

    '''
    if n < 1:
        raise ValueError()
    elif n == 1:
        return 1
    else:
        return fact(n-1)*n


if __name__ == '__main__':
    import doctest
    doctest.testmod()