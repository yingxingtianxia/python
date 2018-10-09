#!/usr/bin/env python
#--coding: utf8--
a = int(raw_input('请输入一个数: '))
b = a >> 4
c = ~(~0 << 4)
d = b & c
print '%o\t%o' % (a,d)