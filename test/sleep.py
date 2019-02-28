#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 暂停一秒输出。
import time
dict = {1: "a", 2: "b"}

for key,value in dict.items():
    time.sleep(1)
    print(key,dict[key])

# 暂停一秒输出，并格式化当前时间。
