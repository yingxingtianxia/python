#!/usr/bin/env python
#--coding: utf8--
#操作符重载
class Number(object):
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other

    def __radd__(self, other):
        return self.num + other

    def __sub__(self, other):
        return self.num - other

    def __rsub__(self, other):
        return other - self.num

    def __mul__(self, other):
        return self.num * other

    def __rmul__(self, other):
        return other * self.num

    def __div__(self, other):
        return self.num / other

    def __rdiv__(self, other):
        return other / self.num

if __name__ == '__main__':
    a = Number(10)
    print a + 5
    print 5 + a
    print a - 5
    print 5 - a
    print a * 5
    print 5 * a
    print a / 5
    print 5 / a