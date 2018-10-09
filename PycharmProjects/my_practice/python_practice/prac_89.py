#!/usr/bin/env python
#--coding: utf8--
def jiami(num):
    new_num = ''
    for item in num:
        item = int(item)
        new_item = (item+5) % 10
        new_num += str(new_item)
    print new_num[::-1]

if __name__ == '__main__':
    num = raw_input('请输入一个四位数：')
    jiami(num)