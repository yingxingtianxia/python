#!/usr/bin/env python
#--coding: utf8--
def count(x=1, y=2):
    sum = 0

    for i in range(1, y+1):
        num = int(str(x) * i)
        if i == y:
            print num
        else:
            print num , '+',
        sum += num
    print '结果是：', sum

if __name__ == '__main__':
    count()
    count(5,5)