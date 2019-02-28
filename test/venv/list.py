#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 将一个列表的数据复制到另一个列表中。
import copy
list1 = [1,2,3,4,5,6,7,[2,3]]
list2 = []

for i in list1:
    list2.append(i)

# 方法一（ list.copy() 方法只能 copy 一层，这就是所谓的浅复制）

print(list2)


# 实现浅复制的三种方法
list3 = list1.copy()
list4 = list1[:]
list5 = list(list1)
list1[0] = "hello"
list1[7][0] = "test"
print(list1)
print(list3)
print(list4)
print(list5)

# 深复制的方法
names = ["小红", "小黄", "小明", ["小白", "小黑"]]
names1 = copy.deepcopy(names)
names[3][1] = "小绿"

print(names)
print(names1)