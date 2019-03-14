#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个
Master，多个Worker。
    如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。
    如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。

多进程模式：
    优点：稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只
        负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式。
    缺点：创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大。
        另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成
        问题。
多线程模式:
    优点：比多进程快一点
    缺点：就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存（致命）。在Windows上，如果一个线程
        执行的代码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但
        是操作系统会强制结束整个进程。

    在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式。由于多线程存在稳定性的问题，IIS的稳定
性就不如Apache。为了缓解这个问题，IIS和Apache现在又有多进程+多线程的混合模式，真是把问题越搞越复杂。

线程切换：

计算密集型 vs IO密集型
    是否采用多任务的第二个考虑是任务的类型。我们可以把任务分为计算密集型和IO密集型。
    计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。
    要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。
    Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。

    IO密集型：
        涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成。（因
        为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都
        是IO密集型任务，比如Web应用。
        IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行
        速度极低的脚本语言，完全无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚
        本语言是首选，C语言最差。

异步IO：
    考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作，单进程单线程模型会导致别的任务无法
    并行执行，因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行。

    充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx就是支
    持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务。在多核CPU上，可以运行多个进程（数量与CPU核心
    数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。

对应到Python语言，单线程的异步编程模型称为协程，
'''