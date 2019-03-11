#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
StringIO:在内存中读写str
    很多时候，数据读写不一定是文件，也可以在内存中读写。
    getvalue()方法用于获得写入后的str。
BytesIO:实现了在内存中读写bytes
    StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
'''
from io import StringIO
# 写入
f = StringIO()
f.write('hello world!')
s = f.readline()
print(s)
print(f.getvalue())

# 读取
f = StringIO('hello!\nhi\nGoodbye')
while True:
    s = f.readline()
    if s != '':
        print(s.strip())
    else:
        break

'''

'''
from io import BytesIO
f = BytesIO()
f.write('hello byteio'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

# 初始化，指针位置为0
stringIo = StringIO('abc')
print(stringIo.getvalue())
print(stringIo.tell())

# 写入字母d
stringIo.write('d')
print(stringIo.getvalue())
print(stringIo.tell())

# 移动指针到末尾
stringIo.seek(0,2) #2代表从文件末尾算起。
print(stringIo.getvalue())
print(stringIo.tell())

# 写入字母e
stringIo.write('e')
print(stringIo.getvalue())
print(stringIo.tell())