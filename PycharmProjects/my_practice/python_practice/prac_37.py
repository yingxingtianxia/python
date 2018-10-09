#!/usr/bin/env python
#--coding: utf8--
print '请输入十个数字：\n'

a = []
for i in range(10):
    a.append(int(raw_input('请输入数字：')))
a.sort()
print a