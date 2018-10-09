#!/usr/bin/env python
#--coding: utf8--
def compare(num1, num2):
    maxSum = max(num1, num2)
    minSum = min(num1, num2)
    print '%s 比 %s 大' % (maxSum, minSum)

if __name__ == '__main__':
    a = int(raw_input('请输入第一个数：'))
    b = int(raw_input('请输入第二个数：'))
    compare(a, b)