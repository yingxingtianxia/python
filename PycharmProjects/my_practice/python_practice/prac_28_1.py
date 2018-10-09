#!/usr/bin/env python
#--coding: utf8--
#最简单做法
def age(times=4):
    n = 10
    for i in range(1, times+1):
        n += 2

    return n

if __name__ == '__main__':
    print age()