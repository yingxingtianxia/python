#!/usr/bin/env python
#--coding: utf8--
def count():
    while True:
        num = int(raw_input('请输入一个数字：'))
        res = num ** 2
        if res < 50:
            print '计算结果是：%s' % res
            break
        else:
            print '计算结果是：%s' % res

if __name__ == '__main__':
    count()