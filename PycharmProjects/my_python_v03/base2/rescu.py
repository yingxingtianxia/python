#!/usr/bin/env python3
#--*--coding: utf8--*--
def func1(n):
    if n == 1:
        return n

    return n * func1(n-1)

if __name__ == '__main__':
    print(func1(5))
    print(func1(6))