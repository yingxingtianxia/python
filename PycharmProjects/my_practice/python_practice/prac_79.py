#!/usr/bin/env python
#--coding: utf8--
def str_sort(n=3):
    a_list = []
    for i in range(n):
        strings = raw_input('请输入字符串：')
        a_list.append(strings)
    print '初始顺序是%s' % a_list

    a_list.sort()
    print '排序后的顺序是%s' % a_list

if __name__ == '__main__':
    str_sort()