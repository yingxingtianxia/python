#！/usr/bin/env python3
#--*--coding: utf8--*--
def add(x, y):
    return x + y
a = lambda x, y: x + y          #匿名函数，不推荐使用

if __name__ == '__main__':
    print(add(10, 10))
    print(a(20, 20))