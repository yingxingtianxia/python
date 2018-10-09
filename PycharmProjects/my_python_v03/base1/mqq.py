#!/usr/bin/env python3
#--*--coding: utf8--*--
alist = ['hello', 'nihao', 'hi']

for index in range(len(alist)):
    print('%s: %s' %(index, alist[index]))

for ind, val in enumerate(alist):
    print('%s: %s' % (ind, val))

print(list(reversed(alist)))