#!/usr/bin/env python
#--coding: utf8--
import numpy

def matrix_plus(num=3):
    matrix_a = numpy.random.randint(1, 100, num**2).reshape(num, num)
    matrix_b = numpy.random.randint(1, 100, num**2).reshape(num, num)
    matrix_p = numpy.zeros(shape=(num,num))
    for i in range(num):
        for j in range(num):
            matrix_p[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return matrix_p

if __name__ == '__main__':
    print matrix_plus()