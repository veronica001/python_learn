#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
ThreadLocal:
    在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会
影响其他线程，而全局变量的修改必须加锁

    但是局部变量在多层函数调用时，也很麻烦。可以通过用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程
    对应的Student对象，eg: global_dict[threading.current_thread()]  ,代码写出来有点丑。

    ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事

    ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函
    数都可以非常方便地访问这些资源。

小结
    一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线
    程中各个函数之间互相传递的问题。
'''
import threading

last_student = threading.local()
def process_student():
    std = last_student.student
    print('Process Student , %s (in %s)' % (std, threading.current_thread().name))

def thread_student(name):
    last_student.student = name
    process_student()

t1 = threading.Thread(target=thread_student, args=('SA',), name='Thread-A')
t2 = threading.Thread(target=thread_student, args=('SB',), name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()
# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成
# 全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal
# 内部会处理。
#
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher
# 等等。
