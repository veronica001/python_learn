#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# 日期：2019-03-10 15:50
# 工具：PyCharm
# Python版本：3.6.3

'''
Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出。
小结：
    doctest非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，就可以自动把包含doctest的注释提取出来。用户看文档的
    时候，同时也看到了doctest。
'''


class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kwargs):
        super(Dict, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'dict has no attribute "%s"' % key)

    def __setattr__(self, key, value):
        self[key] = value

# 最后三行当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。
# 所以，不必担心doctest会在非测试环境下执行。
if __name__ == '__main__':
    import doctest
    doctest.testmod()
