#!/usr/bin/env python3
#--*--coding: utf8--*--
class MyClass():
    count = 0
    def __init__(self):
        self.a = 10
        MyClass.count += 1

if __name__ == '__main__':
    print(MyClass.count)
    mc1 = MyClass()
    print(MyClass.count)
    print(MyClass.__dict__)
    print(mc1.__dict__)