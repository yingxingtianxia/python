#!/usr/bin/env python
#--coding: utf8--
#数学方法计算阶乘

def jc(num=5):
    res = 1
    for i in range(1,num+1):
        res *= i

    return res
if __name__ == '__main__':
    print jc(10)