#!/usr/bin/env python
#--coding: utf8--
def sushu(num1=101, num2=200):
    result = []
    for i in range(num1, num2+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)

    return result

if __name__ == '__main__':
    print sushu()
    print '一共有%d个素数' % len(sushu())