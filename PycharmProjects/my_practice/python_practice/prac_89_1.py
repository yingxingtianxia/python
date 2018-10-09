#!/usr/bin/env python
#--coding: utf8--
def jiami(num):
    a_list = []
    b_list = []
    for i in num:
        a_list.append(int(i))

    for i in a_list:
        j = (i+5) % 10
        b_list.append(j)
    b_list.reverse()
    new_num = ''.join(str(i) for i in b_list)

    return new_num


if __name__ == '__main__':
    num = raw_input('请输入一个四位数：')
    print jiami(num)