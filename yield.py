#! /usr/bin/env python
# -*- coding: utf-8 -*

# 该函数在运行中占用的内存会随着参数 n 的增大而增大，如果要控制内存占用，最好不要用 List
def fab(n):
    a,b = 0,1
    x = 0
    L = []
    while x < n:
        a, b = b, a + b
        L.append(a)
        x += 1
    return L


print(fab(6))

# yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
# Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个
# iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b
# 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数
# 的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。
def fab2(n):
    a,b = 0,1
    x = 0
    while x < n:
        a, b = b, a + b
        yield a
        x += 1

for n  in fab2(6):
    print(n)