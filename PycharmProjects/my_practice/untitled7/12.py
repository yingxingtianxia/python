#!/usr/bin/env python3
# -*-coding: utf8-*-
file = open('tt.txt', 'a')
while True:
    contect = input('请输入:')
    if contect == 'q':
        file.close()
        exit()
    else:
        file.write(contect + '\n')
