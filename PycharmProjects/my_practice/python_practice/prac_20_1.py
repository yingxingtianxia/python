#!/usr/bin/env python
#--coding: utf8--
def count(counts=10):
    height = 100
    sum = 100

    for i in range(1, counts):
        sum += height
        height /= 2
    print sum, height

if __name__ == '__main__':
    count(2)