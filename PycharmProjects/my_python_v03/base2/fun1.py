#!/usr/bin/env python3
#--*--coding: utf8--*--
def foo():
    bar()
    print('in-foo')

def bar():
    print('in-bar')

if __name__ == '__main__':
    foo()