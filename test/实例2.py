#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 斐波那契数列。
#  在数学上，费波那契数列是以递归的方法来定义：
#  F0 = 0     (n=0)
#  F1 = 1    (n=1)
#  Fn = F[n-1]+ F[n-2](n=>2)

def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + f(n - 2)

print(f(10))

def f2(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b, a+b
    return a

print(f2(10))


# 输出指定个数的斐波那契数列，可以使用以下代码：

def f3(n):
    fibs = [1,1]
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    for i in range(2,n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
print(f3(10))