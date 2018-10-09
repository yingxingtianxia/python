#!/usr/bin/env python
#--coding: utf8--
n = 0
p = raw_input('请输入一个八进制数：')
for i in range(len(p)):
    n = n * 8 + ord(p[i]) - ord('0')
print n