#!/usr/bin/env python3
#__*__coding: utf8__*__
adic = {
    'a':[1,2,3],
    'b':[4,5,6],
    'c':[7,8,9]
}

keys = list(adic.keys())
for i in range(3):
    for j in keys:
        print(adic[j][i])