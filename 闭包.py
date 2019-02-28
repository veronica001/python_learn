#! /usr/bin/env python
# -*- coding: utf-8 -*-

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