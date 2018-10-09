#!/usr/bin/env python
#--coding: utf8--
def reverse_list(n=3):
    a = []
    for i in range(n):
        counter = int(raw_input('请输入一个数： '))
        a.append(counter)
    print a

    Min = min(a)
    a.remove(Min)
    a.append(Min)

    Max = max(a)
    a.remove(Max)
    a.insert(0,Max)
    print a

if __name__ == '__main__':
    reverse_list()