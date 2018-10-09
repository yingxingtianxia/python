#！/usr/bin/env python3
#--*--coding: utf8--*--
from random import randint
from functools import reduce

def func1(num):
    return num % 2
def func2(num):
    return num * 2
def func3(x, y):
    return x + y

if __name__ == '__main__':
    num_list = [randint(1, 100) for i in range(10)]
    print(num_list)
    print(list(filter(func1, num_list)))
    print(list(filter(lambda x: x % 2, num_list)))
    print(list(map(func2, num_list)))
    print(list(map(lambda x: x * 2, num_list)))
    print(reduce(func3, num_list))
    print(reduce(lambda x, y: x + y, num_list))