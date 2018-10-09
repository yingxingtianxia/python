#!/usr/bin/env python
#--coding: utf8--
def fib(n=10):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    #显示单一月份数据
    print fib()