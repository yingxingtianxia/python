#!/usr/bin/env python
#--coding: utf8--
from random import randint

def make_matrix(num=3):
    matrix = []
    for i in range(num):
        items = []
        for j in range(num):
            item = randint(1, 100)
            items.append(item)
        matrix.append(items)

    return matrix

if __name__ == '__main__':
    a_list = make_matrix()
    b_list = make_matrix()
    print a_list
    print b_list
    c_list = []
    for i in range(3):
        zz = map(lambda a, b:a+b, a_list[i], b_list[i])
        c_list.append(zz)
    print c_list