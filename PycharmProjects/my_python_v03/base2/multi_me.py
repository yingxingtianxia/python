#!/usr/bin/env python3
#--*--coding: utf8--*--
class A():
    def foo(self):
        print('IN A')

class B(A):
    def foo(self):
        print('IN B')

class C(A):
    def foo(self):
        print('IN C')

class D(B, C):
    pass

class E(C, B):
    pass


if __name__ == '__main__':
    d = D()
    e = E()
    d.foo()
    e.foo()