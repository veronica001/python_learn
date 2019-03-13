#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
多进程：
    Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回
    两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

    子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进
    程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

    os模块封装了常见的系统调用，其中就包括fork

'''
import os

# print('statr %s process...' % os.getpid())

# p = os.fork()
# if p == 0:
#     print('i am chile process %s and my parent process is %s' %(os.getpid(), os.getppid()))
# else:
#     print('%s create child process %s' % (os.getpid(), p))

# 由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没
# 有问题的，推荐大家用Mac学Python！
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当
# 有新的http请求时，就fork出子进程来处理新的http请求。

'''
multiprocessing:
    由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
    multiprocessing模块提供了一个Process类来代表一个进程对象
    
    创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要
    简单。
    join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
'''
from multiprocessing import Process
import os

# 子进程执行代码
def run_proc(name):
    print('chile process %s %s start ro running...' % (os.getpid(), name))

# if __name__ == '__main__':
#     print('parent process %s..' % os.getpid())
#     p = Process(target = run_proc, args=('test',))
#     print('process start')
#     p.start()
#     p.join()
#     print('child process stop')

'''
Pool:
    如果要启动大量的子进程，可以用进程池的方式批量创建子进程
    对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加
    新的Process了。
    由于Pool的默认大小是CPU的核数，可同时运行的进程数。
'''
from multiprocessing import Pool
import time,random
def long_time_task(name):
    print('Run task,process %s (%s) start' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %f seconds' % (name, (end - start)))

# if __name__ == '__main__':
#     print('process %s is running' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('---------------------------------------------')
#     print('Waiting for all process done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

'''
子进程：
    很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
    subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
    
'''

import subprocess
print('-------------------------')
# print('$ nslookup')
# r = subprocess.call(['nslookup', 'www.python.org'])
# 还需要子进程输入，使用communicate()
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# out,err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(out.decode('utf-8'))
# print('exit code:', p.returncode)

'''
进程间通信：
    Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，
    提供了Queue、Pipes等多种方式来交换数据。
'''
# 以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
from multiprocessing import Process,Queue
# 写数据进程执行代码
def write(q):
    print('write process:', os.getpid())
    for value in ['A', 'b','c']:
        print('write %s to queue' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行代码
def read(q):
    print('read process:', os.getpid())
    while True:
        value = q.get(True)
        print('read %s from queue' % value)

if __name__ == '__main__':
    print('------------main-------------')
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
#     启动子进程写入
    pw.start()
# 启动子进程读取
    pr.start()
#     等待写进程结束
    pw.join()
#     因为读进程是死循环，所以强制结束
    pr.terminate()



'''
小结：
在Unix/Linux下，可以使用fork()调用实现多进程。

要实现跨平台的多进程，可以使用multiprocessing模块。

进程间通信是通过Queue、Pipes等实现的。
'''