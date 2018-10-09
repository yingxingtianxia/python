#!/usr/bin/env python3
# -*-coding: utf8-*-
import car
import
#from car import Car
my_new_car = car.Car("baoba", "760li", "2017")
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 35
my_new_car.read_odometer()
