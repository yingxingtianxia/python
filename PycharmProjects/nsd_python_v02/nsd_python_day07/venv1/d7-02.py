#!/usr/bin/env python
#--coding: utf8--
#局部变量 > 全局变量 > 内建变量
import functools
print len('abcd')

len = 100

def f1():
    len = 200
    print len

def f2():
    print len

f1()
f2()
print len

#print len('hello')         TypeError: 'int' object is not callable



def add(x, y):
    return x + y

add10 = functools.partial(add, 10)
add10(100)