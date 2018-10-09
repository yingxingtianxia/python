#!/usr/bin/env python3
# -*-coding: utf8-*-
def count_words(file_name):
    try:
        with open(file_name) as file_object:
            contects = file_object.read()
    except FileNotFoundError:
        print(file_name + ' this file is not exist')
    else:
        words = contects.split()
        num_words = len(words)
        print('this file has ' + str(num_words) + ' words')


#file_name = 'program.txt'
#count_words(file_name)
file_names = ['gropram.txt', 'test.txt', 'edit.txt']
for file_name in file_names:
    count_words(file_name)