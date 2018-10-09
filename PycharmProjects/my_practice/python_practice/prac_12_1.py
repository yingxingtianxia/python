#!/usr/bin/env python
#--coding: utf8--
from math import sqrt
def sushu(num1=101, num2=200):
    counter = 0
    result = []
    for i in range(num1, num2+1):
        k = int(sqrt(i))
        for j in range(2, k+1):
            if i % j == 0:
                break
        else:
            result.append(i)
            counter += 1

    return result, counter

if __name__ == '__main__':
    sushu()
    print '其中的素数是：%s\n一共有%s个' % (sushu()[0],sushu()[1])