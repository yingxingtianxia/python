#!/usr/bin/env python
#--coding: utf8--
def exchange(a,b):
    a, b = b, a
    return a, b

if __name__ == '__main__':
    a = 10
    b = 20
    print 'a=%s, b=%s' % (a, b)
    res = exchange(a, b)
    print 'a=%s, b=%s' % (res[0], res[1])