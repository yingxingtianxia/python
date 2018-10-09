#!/usr/bin/env python3
#--*--coding: utf8--*--
def fiber(n):
    fiber_list = [0, 1]
    while len(fiber_list) < n:
        new_num = fiber_list[-1] + fiber_list[-2]
        fiber_list.append(new_num)

    print(fiber_list)

if __name__ == '__main__':
    num = int(input("Please enter a number: "))
    fiber(num)