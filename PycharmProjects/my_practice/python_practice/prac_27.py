#!/usr/bin/env python
#--coding: utf8--
#递归函数方法
def output(s, l):
    if l == 0:
        return
    print s[l-1],
    output(s, l-1)

if __name__ == '__main__':
    s = raw_input('Input strings: ')
    l = len(s)
    output(s, l)