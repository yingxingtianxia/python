#!/usr/bin/env python
#--coding: utf8--
def huiwenshu(num1=10000, num2=100000):
    result = []
    for i in range(num1, num2):
        j = str(i)[::-1]
        if i == int(j):
            result.append(i)

    return result

if __name__ == '__main__':
    print huiwenshu()