#!/usr/bin/env python
#--coding: utf8--
def huiwenshu(num1=10000, num2=100000):
    result = []
    for i in range(num1,num2):
        if str(i)[0] == str(i)[4] and str(i)[1] == str(i)[3]:
            result.append(i)

    return result

if __name__ == '__main__':
    print huiwenshu()