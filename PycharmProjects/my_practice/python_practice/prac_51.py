#!/usr/bin/env python
#--coding: utf8--
#python中执行&运算的时候转化为二进制，按位进行
a = 077
b = a & 3
print b
print 'a & b = %d' % b
b &= 3
print 'a & b = %d' % b