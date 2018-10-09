#!/usr/bin/env python
#--coding: utf8--
from random import randint

def bl(n=5):
    a = []
    for i in range(n):
        a.append(randint(1,100))
    print a

    for item in a:
        print item,

    print

    for i in range(len(a)):
        print a[i],

if __name__ == '__main__':
    bl()