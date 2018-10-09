#!/usr/bin/env python3
#--*--coding: utf8--*--
from functools import partial
def add(x, y, z):
    return x + y +z

myadd = partial(add, x=10, y=20)

if __name__ == '__main__':
    print(add(10, 20, 34))
    print(add(10, 20, 19))
    print(myadd(z=10))
