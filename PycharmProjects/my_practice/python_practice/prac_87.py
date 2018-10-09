#!/usr/bin/env python
#--coding: utf8--
class Student():
    x = 0
    c = 0

def f(stu):
    stu.x = 20
    stu.c = 'c'

a = Student()
a.x = 3
a.c = 'a'

f(a)
print a.x, a.c