#!/usr/bin/env python
#--coding: utf8--
def rabbits(n=10):
    a = 1
    b = 1
    if n == 1 or n == 2:
        print '1'
    else:
        for i in range(n-1):
            a, b = b, a+b
            print a,

if __name__ == '__main__':
    #显示列表
    rabbits()