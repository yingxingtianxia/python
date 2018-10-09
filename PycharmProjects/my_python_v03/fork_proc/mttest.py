#!/usr/bin/env python3
#__*__coding: utf8__*__
import threading
import time

a = 10

def add1():
    global a
    time.sleep(1)
    a += 5
    print('in add1 a is', a)

def add2():
    global a
    time.sleep(1)
    a += 100
    print('in add2 a is', a)

t1 = threading.Thread(target=add1)
t2 = threading.Thread(target=add2)

t1.start()
t2.start()

print('a is', a)