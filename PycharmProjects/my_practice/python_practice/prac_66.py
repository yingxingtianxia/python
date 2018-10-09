#!/usr/bin/env python
#--coding: utf8--
def compare():
    num1 = int(raw_input('请输入第一个数：'))
    num2 = int(raw_input('请输入第二个数：'))
    Maxnum = max(num1, num2)
    Minnum = min(num1, num2)

    num3 = int(raw_input('请输入第三个数：'))
    if num3 == Maxnum:
        print Minnum, '<', Maxnum, '=', num3
    elif num3 == Minnum:
        print num3, '=', Minnum, '<', Maxnum
    elif Maxnum < num3:
        print Minnum, '<', Maxnum, '<', num3
    elif num3 < Minnum:
        print num3, '<', Minnum, '<', Maxnum
    else:
        print Minnum, '<', num3, '<', Maxnum

if __name__ == '__main__':
    compare()