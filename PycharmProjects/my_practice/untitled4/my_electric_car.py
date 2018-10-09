#!/usr/bin/env python3
# -*-coding: utf8-*-

from car import ElectricCar

my_tesla = ElectricCar("tesla", "model s", "2017")

print(my_tesla.get_descriptive_name())

my_tesla.battery.battery_size = 90
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
