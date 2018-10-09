#!/usr/bin/env python3
#--*--coding: utf8--*--
import keyword
import string

first_chs = string.ascii_letters + '_'
all_chs = first_chs + string.digits

def check_id(idt):
    if idt[0] not in first_chs:
        return '1st char invalid.'

    for ind, cha in enumerate(idt[1:]):
        if cha not in all_chs:
            return '第%s个字符%s非法' % (ind+2, cha)

    if idt in keyword.kwlist:
        return '%s为关键字' % idt

    return '合法字符'


if __name__ == '__main__':
    idt = input('请输入带检测的标示符：')
    print(check_id(idt))