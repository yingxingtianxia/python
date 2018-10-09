#!/usr/bin/env python
#--coding: utf8--
from random import randint

def p_star(n=7):
    for i in range(n):
        num = randint(1,51)
        print '*' * num

if __name__ == '__main__':
    p_star()