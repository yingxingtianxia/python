#!/usr/bin/env python
#--coding: utf8--
def count():
    strings = raw_input('请输入字符串：')
    letters, digitals, spaces, others = 0, 0, 0, 0

    for item in strings:
        if item.isalpha():
            letters += 1
        elif item.isdigit():
            digitals += 1
        elif item.isspace():
            spaces += 1
        else:
            others += 1

    return letters, digitals, spaces, others

if __name__ == '__main__':
    result = count()
    print '字母有%s个\n数字有%s个\n空格有%s个\n其他字符有%s个' % (result[0], result[1], result[2], result[3])