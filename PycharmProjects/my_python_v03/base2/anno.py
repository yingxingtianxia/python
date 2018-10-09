#!/usr/bin/env python3
#--*--coding: utf8--*--
from random import randint

def func1(n):
    return n % 2

if __name__ == '__main__':
    num_list = [randint(1,100) for i in range(10)]
    print(num_list)
    a = filter(func1, num_list)
    print(list(a))