#!/usr/bin/env python3
#--*--coding: utf8--*--
class User(object):

    def __init__(self, number):
        self.number = number
        self.number_2 = 0

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def set_number_2(self, number2):
        self.number_2 = number2

    def get_number_2(self):
        return self.number_2

u = User(25)
print(u.get_number())
print(u.number)
u.set_number_2(18)
print(u.get_number_2())
print(u.number_2)