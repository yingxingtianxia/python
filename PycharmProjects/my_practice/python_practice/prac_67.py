#!/usr/bin/env python
#--coding: utf8--
def reverse_list(n=3):
    a = []
    for i in range(n):
        counter = int(raw_input('请输入一个数：'))
        a.append(counter)
    print a
    for i in range(len(a)):
        if a[i] == max(a):
            a[0], a[i] = a[i], a[0]
    for i in range(len(a)):
        if a[i] == min(a):
            a[i], a[len(a)-1] = a[len(a)-1], a[i]

    print a

if __name__ == '__main__':
    reverse_list(5)
