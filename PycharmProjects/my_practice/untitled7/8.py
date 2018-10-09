#!/usr/bin/env python3
# -*-coding: utf8-*-
print('give me two numbers, and i will devide them')
print('enter "q" to quit this program')

while True:
    first_number = input('first number: ')
    if first_number == 'q':
        break
    second_number = input('second number: ')
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can't devide by 0")
    else:
        print('number')
