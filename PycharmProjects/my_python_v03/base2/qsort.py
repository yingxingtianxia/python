#!/usr/bin/env python3
#--*--coding: utf8--*--
from random import randint

def qsort(data):
    data = list(data)
    if len(data) == 0 or len(data) == 1:
        return data

    middle = data.pop()
    smaller = []
    larger = []
    for item in data:
        if item > middle:
            larger.append(item)
        else:
            smaller.append(item)

    return qsort(smaller) + [middle] + qsort(larger)



if __name__ == '__main__':
    nums = [randint(1,100) for i in range(10)]
    print(nums)
    print(qsort(nums))
    astr = 'djfalsjfdla'
    print(qsort(astr))
    atouple = (12,344,32,534,56,3,2,5,555,3244)
    print(qsort(atouple))