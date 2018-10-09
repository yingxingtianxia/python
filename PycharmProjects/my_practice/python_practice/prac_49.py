#!/usr/bin/env python
#--coding: utf8--

Max = lambda x, y: (x > y) * x + (x < y) * y
Min = lambda x, y: (x < y) * x + (x > y) * y

if __name__ == '__main__':
    a = 10
    b = 20
    print 'The large one is %d' % Max(a,b)
    print 'The small one is %d' % Min(a,b)