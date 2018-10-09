#!/usr/bin/env python3
# -*-coding: utf8-*-
from car import Car, ElectricCar

my_beetle = Car("volsswagen", "beetle", "2015")
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "medel s","2017")
print(my_tesla.get_descriptive_name())