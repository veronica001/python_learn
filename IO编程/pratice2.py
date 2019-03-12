#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
# 2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

    os.path.basename() 去掉目录路径, 返回文件名
    os.chdir() 方法用于改变当前工作目录到指定的路径。
'''
import os

#获取目录下的文件
def findStr(path, str):
    list = os.listdir(path)
    # 切换到当前目录
    for f in list:
        ff = f if path == '.' else path+'/'+f
        if os.path.isfile(ff):
            if os.path.splitext(f)[0].find(str) != -1:
                print('%-10s: %-20s' % (f, path))
            continue
        else:
            # path = path + '/' + f
            path = os.path.join(path, f) #和上一行效果一样
            # if not os.listdir(path):
            findStr(path, str)
        path = path[:-(len(f)+1)]


findStr('.', 'test')



# 下边是别人的例子，可以参考，但是没打印相对路径
str_ = 'test'
os.chdir(r'E:\MyCode\python\IO编程') #测试用目录
def find():
    #查找当前目录下包含'answer'的文件并打印
    filepath_list = [x for x in os.listdir() if os.path.isfile(x) and str_ in x]
    for i in filepath_list:
        print('%-10s : %s' % (i, '.'))
    #查找当前目录的子目录
    subfolder_list =[x for x in os.listdir() if os.path.isdir(x)]
    #在子目录中循环
    for i in subfolder_list:
        os.chdir(i)     #切换当前目录为子目录i
        find()          #递归调用
        os.chdir('..')
# find()
