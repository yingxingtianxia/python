#!/usr/bin/env python
#--coding: utf8--
def fib(n=5):
    if n == 1:
        print '1'
    elif n == 2:
        print '1 1'
    else:
        a, b = 0, 1
        while n:
            a, b, n = b, b+a, n-1
            print a,

if __name__ == '__main__':
    fib(10)