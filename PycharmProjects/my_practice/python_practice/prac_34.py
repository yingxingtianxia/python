#!/usr/bin/env python
#--coding: utf8--
def one():
    print 'Hello'

def two():
    return  'Hi'

def three(hi='Nice to meet you'):
    return hi

if __name__ == '__main__':
    one()
    print two()
    print three()
    print three('nihao')