#!/usr/bin/env python
#--coding: utf8--
import numpy

def matrix_plus(num=3):
    matrix_a = numpy.random.randint(1, 100, num**2).reshape(num, num)
    matrix_b = numpy.random.randint(1, 100, num**2).reshape(num, num)
    matrix_p = matrix_a + matrix_b

    return matrix_p

if __name__ == '__main__':
    print matrix_plus()