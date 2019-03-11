#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
调试方法：
1、print ：简单直接粗暴有效，缺点：还得删掉，垃圾信息太多
2、断言：凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
    程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert
    关闭后，你可以把所有的assert语句当成pass来看。
3、logging: 把print替换成logging

'''
import logging
logging.basicConfig(level=logging.INFO)
def foo(s):
    n = int(s)
    # assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    # 如果断言失败，assert语句本身就会抛出AssertionError：
    assert n != 0, 'n is zero!'
    return 10 / n


# foo('0')
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10/n)