#!/usr/bin/env python3
#--*--coding: utf8--*--
class Number():
    def __init__(self, num):
        self.num = num

    def __add__(self, other):           #__sub__  __mul__
        return self.num + other

    def __radd__(self, other):
        return self.num + other         #__rsub__ __rmul__

    def __gt__(self, other):
        return self.num > other


if __name__ == '__main__':
    n1 = Number(10)
    print(n1 + 5)
    print(5 + n1)
    print(n1 > 5)