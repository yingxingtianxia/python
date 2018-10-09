#!/usr/bin/env python
#--coding: utf8--
#遍历方法
def back_sort(strings):
    for i in range(1, len(strings)+1):
        print strings[-i],

if __name__ == '__main__':
    info = raw_input('Input strings: ')
    back_sort(info)