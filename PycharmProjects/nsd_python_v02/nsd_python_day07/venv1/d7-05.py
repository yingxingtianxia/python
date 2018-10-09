#!/usr/bin/env python
#--coding: utf8--
from random import randint

def q_sort(num_list):
    if len(num_list) == 0 or len(num_list) == 1:
        return num_list
    middle = num_list.pop()
    smaller = []
    larger = []

    for num in num_list:
        if num < middle:
            smaller.append(num)
        else:
            larger.append(num)

    return q_sort(smaller) + [middle] + q_sort(larger)

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print nums
    print q_sort(nums)