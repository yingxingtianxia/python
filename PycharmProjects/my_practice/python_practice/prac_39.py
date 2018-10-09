#!/usr/bin/env python
#--coding: utf8--
from random import randint

def make_list(num=10):
    re_list = []
    for i in range(num):
        re_list.append(randint(1,100))
    re_list.sort()

    return re_list

def join_list(num, u_list):
    for i in range(len(u_list)-1):
        if u_list[i] <= num < u_list[i+1]:
            u_list.insert(i+1, num)
            break

    return u_list


if __name__ == '__main__':
    u_list = make_list()
    print u_list
    num = int(raw_input('请输入一个数：'))
    print join_list(num, u_list)