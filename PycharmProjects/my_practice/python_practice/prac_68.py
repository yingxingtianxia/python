#!/usr/bin/env python
#--coding: utf8--
import sys
from random import randint

def move(n=5,m=2):
    if m >= n:
        print '数据大小有错误'
        sys.exit()

    a_list = []
    for i in range(n):
        num = randint(1,100)
        a_list.append(num)

    print a_list

    for i in range(m):
        # m_num = a_list.pop()
        # a_list.insert(0, m_num)

        # a_list.insert(0, a_list.pop())

        m_num = a_list[-1]
        a_list.remove(a_list[-1])
        a_list.insert(0, m_num)

    print a_list


if __name__ == '__main__':
    move()