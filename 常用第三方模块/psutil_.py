#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
用Python来编写脚本简化日常的运维工作是Python的一个重要用途。
Python可以通过subprocess模块调用系统命令并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。
在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。它不仅可以通过一两行代码实现系统监控，还可以跨平台使用
psutil = process and system utilities
'''
import psutil

# cpu信息
print('---------------获取cpu信息----------------')
print(psutil.cpu_count()) # CPU逻辑数量
print(psutil.cpu_count(logical=False))# CPU物理核心
# 2说明是双核超线程, 4则是4核非超线程

# 统计CPU的用户／系统／空闲时间
print(psutil.cpu_times())

# 实现类似top命令的CPU使用率，每秒刷新一次，累计10次
for i in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

# 内存信息
print('---------------获取内存信息----------------')
# 获取物理内存和交换内存信息，分别使用：
print(psutil.virtual_memory())
print(psutil.swap_memory())
# 返回的是字节为单位的整数，可以看到，总内存大小是12751032320 = 11.87 GB，已用7239241728 = 6.7 GB，使用了66.6%。
# 而交换区大小是25500119040 = 23.74 GB。

# 获取磁盘信息
print('---------------获取磁盘信息-----------------')
print(psutil.disk_partitions())# 磁盘分区信息
print(psutil.disk_usage('/'))# 磁盘使用情况
print(psutil.disk_io_counters())# 磁盘IO
# 可以看到，磁盘'/'的总容量是304943722496 = 284 GB，使用了3.7%。文件格式是NTFS，opts中包含rw表示可读写，
# journaled表示支持日志。


print('---------------获取网络信息-----------------')
print(psutil.net_io_counters()) # 获取网络读写字节／包的个数
# print('网络接口信息：',psutil.net_if_addrs()) # 获取网络接口信息
# print('网络接口状态',psutil.net_if_stats()) # 获取网络接口状态
# print('当前网络连接信息',psutil.net_connections()) #获取当前网络连接信息

print('--------------获取进程信息--------------------')
print('所有进程id:', psutil.pids())
# 获取指定进程
p = psutil.Process(11864)
print('进程名称：',p.name())
print('路径：', p.exe())
print('进程工作目录：', p.cwd())
print('进程启动的命令行:', p.cmdline())
print('父进程ID:',p.ppid())
print('父进程:',p.parent())
'''
>>> p.children() # 子进程列表
>>> p.status() # 进程状态
'running'
>>> p.username() # 进程用户名
'michael'
>>> p.create_time() # 进程创建时间
1511052731.120333
>>> p.terminal() # 进程终端
'/dev/ttys002'
>>> p.cpu_times() # 进程使用的CPU时间
pcputimes(user=0.081150144, system=0.053269812, children_user=0.0, children_system=0.0)
>>> p.memory_info() # 进程使用的内存
pmem(rss=8310784, vms=2481725440, pfaults=3207, pageins=18)
>>> p.open_files() # 进程打开的文件
[]
>>> p.connections() # 进程相关网络连接
[]
>>> p.num_threads() # 进程的线程数量
1
>>> p.threads() # 所有线程信息
[pthread(id=1, user_time=0.090318, system_time=0.062736)]
>>> p.environ() # 进程环境变量
{'SHELL': '/bin/bash', 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:...', 'PWD': '/Users/michael', 'LANG': 'zh_CN.UTF-8', ...}
>>> p.terminate() # 结束进程
psutil还提供了一个test()函数，可以模拟出ps
'''
print(psutil.test())