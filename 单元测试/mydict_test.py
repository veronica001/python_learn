#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

'''
# 为了编写单元测试，我们需要引入Python自带的unittest模块
import unittest
# from mydict import Dict

# 比如对函数abs()，我们可以编写出以下几个测试用例：
# 1. 输入正数，1， 2.1， 0.99，期待输出与输入一样
# 2. 输入负数， -2， -3.1， -0.88, 期待输出为正数
# 3. 输入0， 期待输出0
# 4. 输入非数值类型，比如None, [], 'a',  期待抛出TpyeError

class Dict(dict):
    def __init__(self, **kwargs):
        super(Dict, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'dict' has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


'''
编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。

以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
最常用的断言就是assertEqual() eg: self.assertEqual(abs(-1), 1) 
另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：
    with self.assertRaises(KeyError):
        value = d['empty']
'''

class TestDict(unittest.TestCase):
    def setUp(self):
        print('setup...')

    def tearDown(self):
        print('teardown....')

    def test_unit(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'testvalue'
        self.assertEqual(d['key'], 'testvalue')
        # self.assertTrue(self, isinstance('key' in d.keys))

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d.key, 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            # 比如通过d['empty']访问不存在的key时，断言会抛出KeyError
            value = d['empty']
            # []可以变量作为索引值，而.不能以变量作为索引值
            # value = d.empty

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            # 通过d.empty访问不存在的key时，我们期待抛出AttributeError
            value = d.empty


if __name__ == '__main__':
    unittest.main()

'''
推荐命令行通过参数-m unittest直接运行单元测试，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试
eg: python -m unittest xxx

可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行
应用场景：
    setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数
    据库，这样，不必在每个测试方法中重复相同的代码：
'''

