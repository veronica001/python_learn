#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。

如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，
Python内置的os模块也可以直接调用操作系统提供的接口函数。
os.name: 操作系统类型。
    posix：说明系统是Linux、Unix或Mac OS X
    nt：就是Windows系统。
uname(): 详细的系统信息,注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
environ:  环境变量。要获取某个环境变量的值，可以调用os.environ.get('key')

操作文件和目录
    操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
'''
import os
print(os.name)
# print(os.uname()
# print(os.environ)
# print(os.environ.get('Path'))

# 查看当前目录德绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，
# 1 把新目录的完整路径表示出来
print(os.path.join('E:/MyCode/python/IO编程', 'testdir1'))
# 2 然后创建目录
print(os.makedirs('E:/MyCode/python/IO编程/testdir1'))
# 删除目录
os.rmdir('E:/MyCode/python/IO编程/testdir1')

'''
把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
    在Linux/Unix/Mac下，os.path.join()返回这样的字符串：part-1/part-2
    而Windows下会返回这样的字符串：part-1\part-2

同样,要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总
是最后级别的目录或文件名

os.path.splitext() :可以直接让你得到文件扩展名
这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。
'''
print(os.path.split('E:/MyCode/python/IO编程/test.txt'))
print(os.path.splitext('E:/MyCode/python/IO编程/test.txt'))

# 重命名
# print(os.rename('test.txt', 'test.py'))
# 删除文件
# os.remove('test.py')

'''
shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
'''
# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出所有.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


