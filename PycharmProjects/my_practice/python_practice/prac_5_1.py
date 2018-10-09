#!/usr/bin/env python
#--coding: utf8--
def quict_sort(times=3):
    list = []
    for i in range(times):
        num = int(raw_input("请输入一个数："))
        list.append(num)
    list.sort()
    for item in list:
        print item,

if __name__ == '__main__':
    quict_sort(5)