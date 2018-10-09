#!/usr/bin/env python
#--coding: utf8--
import time

if __name__ == '__main__':
    date = time.strftime('%m-%d')
    if date == '03-08':
        print '女神节'
    elif date == '02-14':
        print '情人节'
    else:
        print '发红包'
    print '这是一个测试题'