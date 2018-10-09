#!/usr/bin/env python
#--coding: utf8--

def count(func):
    def times(*args):
        return func(*args) * 3
    return times

@count
def wel(name):
    return 'Welcome back %s!' % name

@count
def go():
    return 'Where are you go\t'

@count
def ans(pos):
    return "I'm going to %s\n" % pos

if __name__ == '__main__':
    print wel('tom')
    print go()
    print ans('Beijing')