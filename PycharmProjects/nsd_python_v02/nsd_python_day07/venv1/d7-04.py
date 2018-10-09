#!/usr/bin/env python
#--coding: utf8--
#递归函数
def f1(num):
    if num == 1:
        return num
    return num * f1(num - 1)

if __name__ == '__main__':
    print f1(5)
    print f1(6)