#!/usr/bin/env python
#--coding: utf8--
test_list = ['a', 'b', 'c', 'd']
def one():
    re_list = test_list[::-1]
    print re_list

def two():              #执行结果会修改全局变量test_list
    test_list.reverse()
    print test_list

def three():
    re_list = []
    for i in range(1, len(test_list)+1):
        re_list.append(test_list[-i])
    print re_list


if __name__ == '__main__':
    one()
    two()
    three()