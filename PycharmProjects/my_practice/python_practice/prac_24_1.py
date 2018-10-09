#!/usr/bin/env python
#--coding: utf8--
from fractions import Fraction

def count(times=10):
    a = 1
    b = 1
    sum = 0
    result = []
    p_result = []

    for i in range(1, times+1):
        a, b = b, a+b
        num = Fraction(b,a)
        print num,
        sum += num

    print '\n结果是：%s' % sum
if __name__ == '__main__':
    count()