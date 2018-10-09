#!/usr/bin/env python
#--coding: utf8--
a = []
for i in range(10):
    a.append(int(raw_input('请输入一个数： ')))
print a

for x in range(9):
    for y in range(x+1, 10):
        if a[x] > a[y]:
            a[x], a[y] = a[y], a[x]

print a