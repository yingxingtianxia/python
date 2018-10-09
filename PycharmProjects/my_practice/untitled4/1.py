#!/usr/bin/env python3
# -*-coding: utf8 -*-
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' is now roll_over')

my_dog = Dog("willie", "6")
your_dog = Dog("lucy", "3")

print("My dog's name is " + my_dog.name.title()+ ".")
print("Your dog's name is " + your_dog.name.title()+ ".\n")
print("My dog is " + str(my_dog.age) + " years old.")
print("Your dog is " + str(your_dog.age) + " years old.\n")

my_dog.sit()
my_dog.roll_over()
print()
your_dog.sit()
your_dog.roll_over()

