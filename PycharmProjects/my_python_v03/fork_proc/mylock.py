#!/usr/bin/env python3
#__*__coding: utf8__*__
import threading
import time

l = threading.Lock()
a = 10

def add1():
    l.acquire()
    global a
    time.sleep(2)
    a += 5
    print('in add1 a is', a)
    l.release()

def add2():
    l.acquire()
    global a
    time.sleep(2)
    a += 100
    print('in add2 a is', a)
    l.release()

t1 = threading.Thread(target=add1)
t2 = threading.Thread(target=add2)

t1.start()
t2.start()
t1.join()
t2.join()

print('a is', a)