#! /usr/bin/env python
# -*- coding: utf-8 -*-
import math

def quadratic(a, b, c):
    tmp = math.sqrt(b * b - (4*a*c) )
    x1 = (-b + tmp) / (2 * a)
    x2 = (-b - tmp) / (2 * a)
    return x1,x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3))
print(calc(1,3,5,7))
print(calc(1,2))
print(calc())