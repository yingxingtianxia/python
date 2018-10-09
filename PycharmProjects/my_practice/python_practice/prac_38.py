#!/usr/bin/env python
#--coding: utf8--
from random import randint

def make_matrix(num=3):
    matrix = []
    for i in range(num):
        items = []
        for j in range(num):
            item = randint(1, 100)
            items.append(item)
        matrix.append(items)

    return matrix

def count(matrix):
    sum = 0
    for i in range(len(matrix[0])):
        sum += matrix[i][i]

    return sum

if __name__ == '__main__':
    matrix = make_matrix()
    print matrix
    print count(matrix)