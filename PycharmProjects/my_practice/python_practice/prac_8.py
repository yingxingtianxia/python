#!/usr/bin/env python
#--coding: utf8--
def chengfb(number=9):
    for i in range(1, number+1):
        print
        for j in range(1, i+1):
            print '%d * %d = %d\t' % (j, i, i*j),

if __name__ == '__main__':
    chengfb()