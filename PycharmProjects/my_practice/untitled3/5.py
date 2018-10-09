#!/usr/bin/env python3
# -*-coding: utf8-*-

a = input("Please enter the first number: ")
b = input("Please enter the second number: ")
c = input("Plesae enter the third number: ")

if int(a) + int(b) > int(c) and int(a) + int(c) > int(b ) and int(b) + int(c) > int(a):
    print("This three number can form to a triangle.")
    if int(a) == int(b) == int(c):
        print("This three number can form to a equilateral triangle.")
    elif int(a) == int(b) != int(c) or int(a) == int(c) != int(b) or int(b) == int(c) !=int(a):
        print("This three number can form to a isosceles triangle.")
    elif int(a)^2 + int(b)^2 == int(c)^2 or int(a)^2 + int(c)^2 == int(b)^2 or int(b)^2 +int(c)^2 == int(a)^2:
        print("This three number can form to a right triangle")
    else:
        print("This three number can form to a general triangle")
else:
    print("This three number can't form to a triangle")

