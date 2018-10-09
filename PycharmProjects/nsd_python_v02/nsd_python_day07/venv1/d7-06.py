#!/usr/bin/env python
#--coding: utf8--
def count(start=0):
    counter = [start]           #作用于流浪作用域，定义为可变变量
    def incr():
        counter[0] += 1
        return counter[0]
    return incr

if __name__ == '__main__':
    a = count()
    b = count(10)
    print a()
    print a()
    print b()
    print b()
    print a()
    print b()