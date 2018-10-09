#!/usr/bin/env python
#--coding: utf8--
#运用递归函数的思想
def fact(i=5):
    res = 0
    if i == 0:
        res = 1
    else:
        res = i * fact(i-1)

    return res

if __name__ == '__main__':
    print fact()