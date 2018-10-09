#!/usr/bin/env python
#--coding: utf8--
from sys import stdout

def groph(num=10):
    a = []
    for i in range(num):
        a.append([])
        for j in range(num):
            a[i].append(0)
    for i in range(num):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2, num):
        for j in range(1,i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(num):
        for j in range(i+1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print

if __name__ == '__main__':
    groph()