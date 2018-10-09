#!/usr/bin/env python
#--coding: utf8--
class MyClass(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

if __name__ == '__main__':
    a = MyClass(name = 'bob', age = 23)
    print a.name
    print a.age