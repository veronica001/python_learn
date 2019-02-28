#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def creatCounter():
    f = [0]
    print('--闭包外--')
    def counter():
        print('--闭包内--')
        f[0] = f[0] + 1
        return f[0]
    return counter


counterA = creatCounter()
print(counterA(), counterA(), counterA())