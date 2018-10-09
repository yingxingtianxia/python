#!/usr/bin/env python
#--coding: utf8--
from random import randint
from collections import deque
import sys

def move(n=5,m=2):
    if m >= n:
        print '数据采用有错误'
        sys.exit()

    a_list = []
    for i in range(n):
        num = randint(1,100)
        a_list.append(num)
    print a_list

    f = deque(a_list)
    f.rotate(m)
    print list(f)

if __name__ == '__main__':
    move()