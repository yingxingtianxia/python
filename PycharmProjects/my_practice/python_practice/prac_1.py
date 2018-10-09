#!/usr/bin/env python
#--coding: utf8--
def count():
    cnt = 0
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i != j and j != k and k != i:
                    print i * 100 + j * 10 + k
                    cnt += 1
    print '可以组成的三位数一共有%s个' % cnt

if __name__ == '__main__':
    count()
