#!/usr/bin/env python3
#--*--coding: utf8--*--
def counter(start=0):
    count = start
    def incr():
        nonlocal count
        count += 1
        return count
    return incr()


if __name__ == '__main__':
    a = counter()
    print(a)
    print(a)