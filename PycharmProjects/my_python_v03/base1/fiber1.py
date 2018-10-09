#!/usr/bin/env python3
#--*--coding: utf8--*--
def fiber(l):
    fiber_list = [0, 1]
    for i in range(2, l):
        new_num = fiber_list[i-2] + fiber_list[i-1]
        fiber_list.append(new_num)

    print(fiber_list)

if __name__ == '__main__':
    num = int(input("please enter a number: "))
    fiber(num)
