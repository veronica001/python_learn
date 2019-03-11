#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# 日期：2019-03-09 20:33
# 工具：PyCharm
# Python版本：3.6.3

'''
小结

单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。

单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。

单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。

单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。

'''
import unittest

# 练习：对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if isinstance(self.score, int) or isinstance(self.score, float):
            if self.score < 0 or self.score > 100:
                raise ValueError('score should be 0~100!!')
            if 100 >= self.score >= 80:
                return 'A'
            if 80 > self.score >= 60:
                return 'B'
            return 'C'
        else:
            raise ValueError('score type is wrong')




class TestStudent(unittest.TestCase):
    def setUp(self):
        print('setup...')

    def tearDown(self):
        print('TearDown...')

    def test_80_to_100(self):
        s1 = Student('mike', 80)
        s2 = Student('david', 98)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('test1', 60)
        s2 = Student('test2', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('test1', 59)
        s2 = Student('test2', 0)
        s3 = Student('test3', 5.4)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_other(self):
        s1 = Student('test1', -1)
        s2 = Student('test2', 101)
        s3 = Student('test3', 'a')
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()
        with self.assertRaises(ValueError):
            s3.get_grade()


if __name__ == '__main__':
    unittest.main()
