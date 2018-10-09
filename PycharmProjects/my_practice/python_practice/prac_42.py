#!/usr/bin/env python
#--coding: utf8--
#可通过，变量引用高亮查看变量作用域
num = 2
def autofunc():
    num = 1
    print 'internal block num = %d' % num
    num += 1
for i in range(3):
    print 'The number is %d' % num
    num += 1
    autofunc()