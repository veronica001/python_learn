#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
正则表达式是一种用来匹配字符串的强有力的武器。
在正则表达式中，如果直接给出字符，就是精确匹配。
    \d ： 匹配一个数字
    \w :    匹配一个字母或数字
    .  :可以匹配任意字符
    \s :  匹配一个空格（包括tab等空白符）
要匹配变长的字符，在正则表达式中，
    * : 表示任意个字符（包括0个），
    + : 表示至少一个字符，
    ? : 表示0个或1个字符，
    {n} : 表示n个字符，
    {n,m} : 表示n-m个字符

要做更精确地匹配，可以用 [] 表示范围：
    [0-9a-zA-Z\_] ：匹配一个数字、字母或者下划线；
    [0-9a-zA-Z\_]+ ：匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
    [a-zA-Z\_][0-9a-zA-Z\_]* ：匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，
    也就是Python合法的变量；
    [a-zA-Z\_][0-9a-zA-Z\_]{0, 19} ：更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
    A|B ：匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
    ^ : 表示行的开头，^\d 表示必须以数字开头。
    $ : 表示行的结束，\d$ 表示必须以数字结束。

re模块：
    Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意。
    建议使用Python的r前缀，就不用考虑转义的问题
    match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。

切分字符串：
    用正则表达式切分字符串比用固定的字符更灵活
    >>> re.split(r'\s+', 'a b   c')
    ['a', 'b', 'c']
    无论多少个空格都可以正常分割。加入,试试：
    >>> re.split(r'[\s\,]+', 'a,b, c  d')
    ['a', 'b', 'c', 'd']
    再加入;试试：
    >>> re.split(r'[\s\,\;]+', 'a,b;; c  d')
    ['a', 'b', 'c', 'd']

分组：
    除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
    如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
    注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。

贪婪匹配
    最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。

编译
    当我们在Python中使用正则表达式时，re模块内部会干两件事情：
        1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
        2.用编译后的正则表达式去匹配字符串。
    如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步
    骤了，直接匹配
'''
import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

m = re.match(r'^(\d{3})\-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m2 = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2'
              r'[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m2.groups())

print(re.match(r'^(\d+)(0*)$', '102300').groups())
# ('102300', '')  由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配

print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 编译
# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
re_tel = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用
print(re_tel.match('010-12354').groups())

# 练习
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email
#     someone@gmail.com
#     bill.gates@microsoft.com
reg = r'^[\w.]+@[\w.]+$'
def is_valid_email(str):
    m = re.match(reg, str)
    if m != None:
        return True
    else:
        return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
# 版本二可以提取出带名字的Email地址：
#     <Tom Paris> tom@voyager.org => Tom Paris
#     bob@example.com => bob
reg_name = r'^(<([\w\s]+)>)?\s*([\w]+(\.[\w]+)*)@[\w]+(\.[\w]+)*$'

def name_of_email(str):
    rst = re.match(reg_name, str)
    if rst:
        g = rst.groups()
        if g[1]:
            return g[1]
        else:
            return g[2]
    else:
        return None


assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')