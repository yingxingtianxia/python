#!/usr/bin/env python
#--coding: utf8--
from random import randint

def s_e(n=5):
    a_list = []
    b_list = []
    for i in range(n):
        a_list.append(randint(1,100))
        b_list.append(randint(1,100))
    print a_list
    print b_list

    a_list.sort()
    b_list.sort()
    print a_list
    print b_list

    print  a_list + b_list
    a_list.extend(b_list)
    print a_list
    b_list.extend(a_list)
    print b_list

if __name__ == '__main__':
    s_e()