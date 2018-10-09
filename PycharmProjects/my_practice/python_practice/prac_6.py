#!/usr/bin/env python
#--coding: utf8--
def fib(n=10):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fibs = [1, 1]
        for i in range(2, n):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs

if __name__ == '__main__':
    print fib(3)