#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time,random,queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

def get_task():
    return task_queue

def get_result():
    return result_queue

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 多进程需要在main函数中运行，
if __name__ == '__main__':
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    # windows下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
    QueueManager.register('get_task_queue', callable=get_task)
    # register(cls, typeid, callable=None, proxytype=None, exposed=None,
    #                  method_to_typeid=None, create_method=True)
    # register 有个参数create_mothed，默认是True,就是默认写一个方法，也就是 def get_task_queue(): pass
    QueueManager.register('get_result_queue', callable=get_result)

    # 绑定端口5000, 设置验证码'abc':
    #绑定端口并设置验证码，windows下需要填写ip地址，linux下不填默认为本地
    manager = QueueManager(address=('127.0.0.1', 5000), authkey = b'abc')
    # 启动Queue:
    manager.start()

    # 通过网络获取任务队列和结果队列
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去:
    for i in range(10):
        t = random.randint(0,1000)
        print('put task:',t)
        task.put(t)

    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('get result: ', r)
    # 关闭:
    manager.shutdown()
    print('manager exit..')