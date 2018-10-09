#!/usr/bin/env python
#--coding: utf8--
b=input('input a number:\n')

a=9
n=1
while (1):
    if a%b==0:
        break
    else:
        a=a*10+9
        n=n+1
print '%d 个 9 除于 %d 为整数' % (n,b)