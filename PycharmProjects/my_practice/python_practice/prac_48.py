#!/usr/bin/env python
#--coding: utf8--
def compare(num1, num2):
    if num1 < num2:
        print '%s 小于 %s' % (num1, num2)
    elif num2 > num2:
        print '%s 大于 %s' % (num1, num2)
    else:
        print '%s 等于 %s' % (num1, num2)

if __name__ == '__main__':
    num1 = int(raw_input('请输入第一个数： '))
    num2 = int(raw_input('请输入第二个数： '))
    compare(num1, num2)