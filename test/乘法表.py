#! /usr/bin/env python
# -*- coding: utf-8 -*-

for i in range(1,10):
    for j in range(1,i+1):
        print(j,"*",i,"=",i*j,' ',end='')
        #两种写法都行
       # print("%d*%d=%d " %(j,i,i*j), end='')
    print(" ")