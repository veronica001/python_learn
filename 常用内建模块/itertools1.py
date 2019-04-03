#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
itertools:
    Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
    首先，我们看看itertools提供的几个“无限”迭代器

chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
groupby()把迭代器中相邻的重复元素挑出来放在一起
itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
'''
import itertools
natuals = itertools.count(1)
# for n in natuals:
    # print(n)

# 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。

# cycle()会把传入的一个序列无限重复下去，同样停不下来
cs = itertools.cycle('abc')
# for c in cs:
    # print(c)

'''
无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在
内存中创建无限多个元素。

无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
'''
ns = itertools.takewhile(lambda x: x <= 10 ,natuals)
# print(list(ns))

# for i in itertools.chain('ABC', 'DEF'):
#     print(i)

'''
挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。
如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
'''
# for key, group in itertools.groupby('AAABBBAaCCCB', lambda c: c.upper()):
    # print(key, list(group))

# 练习
# 计算圆周率可以根据公式：
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd = itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odd_n = itertools.takewhile(lambda x: x <= (2*N -1), odd)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    sum = 0
    f = 4
    cs = itertools.cycle([4,-4])
    # for i in odd_n:
        # 自己写的
        # if count % 2 == 0:
        #     tmp = 4/i
        # else:
        #     tmp = -1/i
        # step 4: 求和:
        # 网上看的
        # sum += f/i
        # f = - f
    # #另一种方法
    for i in range(N):
        sum += next(cs)/next(odd)
    return sum

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')