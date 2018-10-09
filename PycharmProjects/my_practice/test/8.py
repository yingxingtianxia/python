#!/usr/bin/env python3
# -*-coding: utf8-*-
text = input("enter a number: ")
n = int(text)
if n <= 3:
    print("spring")
elif 3 < n <= 6:
    print("summer")
else:
    print("winter")
print("exit of program")