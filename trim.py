#! /usr/bin/env python
# -*- coding: utf-8 -*-

def trim(s):
    if len(s) == 0:
        return s
    elif s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-2])
    else:
        return s


def trim1(s):
    if 0 == len(s):
        return s
    while ' ' == s[0]:
        s = s[1:]
        if 0 == len(s):
            return s
    while ' ' == s[-1]:
        s = s[:-2]
        if 0 == len(s):
            return s


 def trim2(s):
        for i in range(len(s)):
            if s[0] ==' ':
                s = s[1:]
        for k in range(len(s)):
            if s[-1] == ' ':
                s = s[:-1]
        return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

if trim1('hello  ') != 'hello':
    print('测试失败!')
elif trim1('  hello') != 'hello':
    print('测试失败!')
elif trim1('  hello  ') != 'hello':
    print('测试失败!')
elif trim1('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim1('') != '':
    print('测试失败!')
elif trim1('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


if trim2('hello  ') != 'hello':
    print('测试失败!')
elif trim2('  hello') != 'hello':
    print('测试失败!')
elif trim2('  hello  ') != 'hello':
    print('测试失败!')
elif trim2('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim2('') != '':
    print('测试失败!')
elif trim2('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')