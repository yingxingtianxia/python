#!/usr/bin/env python3
#--*--coding: utf8--*--
def foo():
    print('in-foo')
    def bar():
        print('in-foo-bar')
    bar()

if __name__ == '__main__':
    foo()