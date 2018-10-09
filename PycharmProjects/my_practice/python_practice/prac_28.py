#!/usr/bin/env python
#--coding: utf8--
#采用递归函数
def age(n=5):
    if n == 1:
        c = 10
    else:
        c = age(n-1) +2

    return c

if __name__ == '__main__':
    print age()