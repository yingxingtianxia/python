#!/usr/bin/env python
#--coding: utf8--
def count(num=10):
    sum = 0
    for i in range(1, num+1):
        res = 1
        for j in range(1,i+1):
            res *= j
        sum += res

    return sum

if __name__ == '__main__':
    print count(20)