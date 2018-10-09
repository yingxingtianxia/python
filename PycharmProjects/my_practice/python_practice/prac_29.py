#!/usr/bin/env python
#--coding: utf8--
def ope_num(num):
    length = len(num)
    if length > 5:
        print '位数太长，无法计算'
    else:
        print '这个数字是%s位数' % length

        #ope_num = num[::-1]

        ope_num = ''
        for i in range(1,len(num)+1):
            ope_num = num[-i]

        print '这个数的反序输出结果是：%s' % ope_num

if __name__ == '__main__':
    number = raw_input('请输入一个数：')
    ope_num(number)

