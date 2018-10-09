#!/usr/bin/env python
#--coding: utf8--
def grade():
    score = int(raw_input('请输入分数：'))
    if score in range(0, 60):
        return 'C'
    elif score in range(60, 90):
        return 'B'
    elif score in range(90, 101):
        return 'A'
    else:
        return '分数有错'

if __name__ == '__main__':
    print grade()