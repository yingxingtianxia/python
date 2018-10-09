#!/usr/bin/env python
#--coding: utf8--
def graph(num=10):
    a = s = [1]
    for i in range(num):
        for j in range(i+1):
            if j==0 or i==j:
                s.append(1)
                print 1,
            else:
                a.append(a[j]+a[j-1])
                print a[j]+a[j-1],
        print
        a, s = s, []

if __name__ == '__main__':
    graph()