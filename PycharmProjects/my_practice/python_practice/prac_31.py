#!/usr/bin/env python
#--coding: utf8--
import sys

day_list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
f_list = ['M', 'T', 'W', 'F', 'S']
s_list = ['u', 'h', 'a']
while True:
    first_string = raw_input('请输入第一个字母：')
    if first_string == 'q':
        print '退出程序'
        break
    elif first_string.upper() not in f_list:
        print '输入有误'
        continue
    else:
        if first_string.upper() == 'M':
            print 'Today is Monday'
        elif first_string.upper() == 'W':
            print 'Today is Wednesday'
        elif first_string.upper() == 'F':
            print 'Today is Friday'
        else:
            while True:
                second_string = raw_input('请输入第二个字母：')
                if second_string == 'q':
                    print '退出程序'
                    sys.exit()
                elif second_string not in s_list:
                    print '输入有错'
                    continue
                else:
                    if second_string == 'h':
                        print 'Today is Thursday'
                    elif second_string == 'a':
                        print 'Today is Saturday'
                    else:
                        if first_string.upper() == 'T':
                            print 'Today is Tuesday'
                        else:
                            print 'Today is Sunday'
                    break