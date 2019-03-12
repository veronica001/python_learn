#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
# 练习
# 1.利用os模块编写一个能实现dir -l输出的程序。
# 显示最近修改时间，文件类型，文件大小，名称
os.path.getatime(path) 	返回最近访问时间（浮点型秒数）
os.path.getmtime(path) 	返回最近文件修改时间
os.path.getctime(path) 	返回文件 path 创建时间
os.path.getsize(path) 	返回文件大小，如果文件不存在就返回错误
os.path.isfile(path) 	判断路径是否为文件
os.path.isdir(path) 	判断路径是否为目录
%-10s
“-”是左对齐。，10表示占10个字符空间，不足10个用空格代替
%10s：默认是右对齐
'''
import os
import time
import datetime
list = os.listdir('.')
print('Last Modify              Size      Type      Name')
print('------------------------------------------------')
for x in list:
    t = os.path.getmtime(x) #最近修改时间
    format_t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))
    size = os.path.getsize(x)
    type = '<DIR>' if os.path.isdir(x) else ''
    print('%-25s%-10d%-10s%-15s' % (format_t, size, type, x))

# 示例答案
from datetime import datetime
import os

pwd = os.path.abspath('.') #获取了绝对路径

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))