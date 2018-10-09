#!/usr/bin/env python
#--coding: utf8--
l1 = [1, 2, 3]
l2 = ['aa', 'bb', 'cc']
print {l1[i]:l2[i] for i in range(len(l1))}
d = {}

for index in range(len(l1)):
    d[l1[index]] = l2[index]

print d

for i in range(len(l1)):
    d.setdefault(l1[i], l2[i])
print d

