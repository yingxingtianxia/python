#!/usr/bin/env python
#--coding: utf8--
import numpy as np

def make_matrix(num=3):
    matrix = np.random.randint(1,100,num**2).reshape(num,num)

    return matrix

def count(matrix):
    length = len(matrix[0])
    sum = 0
    for i in range(length):
        sum += matrix[i][i]

    return sum

if __name__ == '__main__':
    matrix = make_matrix()
    print matrix
    print '对角线相加的结果是%s' % count(matrix)