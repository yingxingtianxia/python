#!/usr/bin/env python3
#--*--coding: utf8--*--
class A():
    def foo(self):
        print('a method')

class B():
    def bar(self):
        print('b method')

class C(A, B):
    pass


if __name__ == '__main__':
    c = C()
    c.foo()
    c.bar()