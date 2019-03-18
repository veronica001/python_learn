#! /usr/bin/env python
# -*- coding: utf-8 -*-

def is_palindrome(n):
    # 计算一共多少个数字
    num = 1
    tmp = n
    if n < 10:
        return 1
    else:
        while tmp // 10 > 0:
            num += 1
            tmp = tmp // 10
        # 比较位数
        half = num // 2
        # 取前边z位数值
        x = num - half
        y = 10
        while x > 1:
            y = y * 10
            x -= 1
        front = n // y
        back = n % y
        if num % 2 != 0:
            back = back % (y // 10)
        if front == back:
            return 1
        else:
            return 0

def is_palindrome1(n):
    s = str(n)
    num = int(len(s)/2)
    if num == 0:
        return True
    elif s[:num] == s[-num:]:
        return True
    else:
        return False


def is_palindrome2(n):
    return str(n) == str(n)[::-1]

def is_palindrome3(n):
    m = str(n)
    x = m[::-1]
    if n/int(x) == 1:
        return n

def is_palindrome(n):
    return n == int(str(n)[::-1])
# 测试:
output = filter(is_palindrome2, range(1, 1000))
print(output)
print('1~1000:', list(output))
if list(filter(is_palindrome2, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')