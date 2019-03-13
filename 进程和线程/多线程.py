#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
多线程：
    多任务可以由多进程完成，也可以由一个进程内的多线程完成。
    进程是由若干线程组成的，一个进程至少有一个线程。
    由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正
    的Posix Thread，而不是模拟出来的线程。

Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数
情况下，我们只需要使用threading这个高级模块。

'''
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
import time, threading

# 新建的线程执行的代码
# def loop():
#     print('Thread %s is running' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('Thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('Thread %s ended' % threading.current_thread().name)
#
# print('Thread %s is running ' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='loopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)
# 由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个
# current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用
# LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1
# ，Thread-2……

'''
Lock:
    多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量
    都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一
    个变量，把内容给改乱了。

    高级语言的一条语句在CPU执行时是若干条语句
    balance = balance + n
        计算balance + n，存入临时变量中: x = balance + n
        将临时变量的值赋给balance: balance = x
        
    当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。

    获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定
会被释放。
    
    锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁
    的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图
    获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
'''

# 确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其
# 他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻
# 最多只有一个线程持有该锁，所以，不会造成修改的冲突
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 先获取锁
        lock.acquire()
        try:
            # 放心改吧
            change_it(n)
        finally:
#             改完了一定要释放锁
            lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

'''
多核CPU
    如果你不幸拥有一个多核CPU，你肯定在想，多核应该可以同时执行多个线程。
    因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，
    必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有
    线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
    
    GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的
    解释器。
    所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过
这样就失去了Python简单易用的特点。
    不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的
GIL锁，互不影响。
    '''
'''
小结

多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。

Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
'''