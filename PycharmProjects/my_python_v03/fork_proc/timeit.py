#!/usr/bin/env python3
#__*__coding: utf8__*__
import time
import os
import sys
import threading

def addtest():
    res = 0
    for i in range(50000000):
        res += i
    print(res)

if __name__ == '__main__':
    #单进程单线程
    only_timestart = time.time()
    for i in range(3):
        addtest()
    only_timeend = time.time()
    print('单进程单线程运行时间是', only_timeend-only_timestart)

    #多进程
    fork_timestart = time.time()
    for i in range(3):
        pid = os.fork()
        if not pid:
            addtest()
            sys.exit()
    os.waitpid(-1, 0)
    os.waitpid(-1, 0)
    os.waitpid(-1, 0)
    fork_timeend = time.time()
    print('多进程运行时间是', fork_timeend-fork_timestart)

    #多线程
    th_timestart = time.time()
    threads = []
    for i in range(3):
        t = threading.Thread(target=addtest)
        threads.append(t)
    for i in range(3):
        threads[i].start()
    for i in range(3):
        threads[i].join()
    th_timeend = time.time()
    print('多线程运行时间是', th_timeend-th_timestart)
    



#Python的多线程由于作者范·罗萨姆的设置，Python内部有一个叫GIL（global interrupt lock）的东西，由于这个锁的控制，Python在执行多线程作业时CPU每次只能处理一个线程，其余线程等待，与单进程的执行结果的区别是单进程是逐个任务执行，多线程是将内存进行时间分片，多个线程在独立的时间片上逐个进行，结果的区别就是单进程单线程逐个任务输出结果，多线程是统一输出结果。
#所以，结论是Python在处理大量数据计算的时候多线程的作用并不明显，甚至还不如单进程单线程，但是在高IO的程序中效果就会很明显了，因为IO等待时间远大于CPU处理数据的时间，这就解释了为什么单进程单线程的ping耗时远大于多线程的ping
