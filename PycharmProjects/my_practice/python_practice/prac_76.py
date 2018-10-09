#!/usr/bin/env python
#--coding: utf8--
def count(n):
    sum = 0.0000
    a_list = []
    if n == 1:
        sum = sum + n
    elif n % 2 == 0:
        for i in range(2, n+1, 2):
            sum = sum + 1.0/i

    elif n % 2 == 1:
        for i in range(1, n+1, 2):
            sum = sum + 1.0/i

    return sum

if __name__ == '__main__':
    print count(5)
    print count(6)