#!/usr/bin/env python3
#--*--coding: utf8--*--
def simple_gen():
    yield 100
    yield 'hello world'
    yield [1, 2, 3]


if __name__ == '__main__':
    a = simple_gen()
    for item in a:
        print(item)