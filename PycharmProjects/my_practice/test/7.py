#!/usr/bin/env python3
# -*-coding: utf8-*-
Name = list()
Age = list()
i = 1
student={}
while i < 5:
    Name[i] = input("please input your name:")
    Age[i] = int(input('please input your age:'))
    i = i + 1

for n in range(5):
    student[n] = {'name': Name[n],'age': Age[n]}
print(student)