#!/usr/bin/env python
#--coding: utf8--
import string

def count():
    strings = raw_input('请输入字符串：')
    result = [0, 0, 0, 0, 0]

    for item in strings:
        if item in string.letters:
            result[0] += 1
        elif item in string.digits:
            result[1] += 1
        elif item in string.punctuation:
            result[2] += 1
        elif item in string.swapcase():
            result[3] += 1
        result[4] += 1

    return result

if __name__ == '__main__':
    result = count()
    print '字母有%s个\n数字有%s个\n特殊字符有%s个\n空白字符有%s个\n一共有%s个字符' \
    % (result[0], result[1], result[2], result[3], result[4])
