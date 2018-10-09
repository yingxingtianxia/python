#!/usr/bin/env python3
#--*--coding: utf8--*--
def deco(func):
    def double():
        result = func() * 2
        return result

    return double

@deco
def echo():
    return 'hello'


if __name__ == '__main__':
    print(echo())