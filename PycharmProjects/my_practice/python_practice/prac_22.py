#!/usr/bin/env python
#--coding: utf8--
A = ['a', 'b', 'c']
B = ['x', 'y', 'z']
info = (['a', 'vs', 'x'], ['c', 'vs', 'x'], ['c', 'vs', 'z'])
match_list = []

for i in A:
    for j in B:
        if [i, 'vs', j] in info:
            continue
        else:
            match_list.append([i, 'vs', j])

print match_list