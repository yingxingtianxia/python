#!/usr/bin/env python
#--coding: utf8--
class A(object):
    def get_name(self):
        print 'In A'

    def pstar(self):
        print '*' * 20

class B(object):
    def dis_name(self):
        print 'In B'

    def pstar(self):
        print '#' * 20

#class C(A, B):
class C(B, A):                      #子类继承多个父类时，查找顺序是从下到上，从左到右
    pass

if __name__ == '__main__':
    c = C()
    c.get_name()
    c.dis_name()
    c.pstar()