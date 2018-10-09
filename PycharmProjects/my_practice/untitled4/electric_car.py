#!/usr/bin/env python3
# -*-coding: utf8-*-
from car_new import Car
"""One class of battrry"""
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery!")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            range = 300


        message =  "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

"""One class of electiccar"""
class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
