#！/usr/bin/env python3
#--*--coding: utf8--*--
import time
def foo():
    print('in_foo')
    def bar():
        print('in_bar')
    bar()

foo()

