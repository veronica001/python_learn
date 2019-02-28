#! /usr/bin/env python
# -*- coding: utf-8 -*-
#  当函数的参数个数太多，
#  需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
import  functools
max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：
# 10加在左边的原理：
# 因为在执行max2=functools.partial(max, 10)的时候，max2里面已经加入了10，然后在执行max2(5,6,7)的时候再加入参数5，6，7。
ret = max2(5, 6, 7)
print(ret)
# 相当于：
args = (10, 5, 6, 7)
# max(*args)

