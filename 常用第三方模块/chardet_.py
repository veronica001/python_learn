#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
虽然Python提供了Unicode表示的str和bytes两种数据类型，并且可以通过encode()和decode()方法转换，但是，在不知道编码的情况下，
对bytes做decode()不好做。
对于未知编码的bytes，要把它转换成str，需要先“猜测”编码。猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有
很大概率“猜对”。
chardet这个第三方库正好就派上了用场。用它来检测编码，简单易用。
获取到编码后，再转换为str，就可以方便后续处理。
'''
import chardet
print(chardet.detect(b'hello world'))
'''
confidence字段，表示检测的概率是1.0（即100%）。
'''
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))