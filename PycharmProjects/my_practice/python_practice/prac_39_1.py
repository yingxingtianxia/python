#!/usr/bin/env python
#--coding: utf8--
import numpy

def op_list(num=10):
    make_list = numpy.random.randint(1, 100, num)
    make_list.sort()
    make_list = list(make_list)

    return make_list

def join_list(num, u_list):
    for i in range(len(u_list)-1):
        if u_list[i] <= num < u_list[i+1]:
            u_list.insert(i+1, num)
            break

    return u_list

if __name__ == '__main__':
    u_list = op_list()
    print u_list
    num = int(raw_input('请输入一个数：'))
    print join_list(num, u_list)