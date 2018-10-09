#!/usr/bin/env python3
# -*-coding: utf8-*-
"""One class of car"""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 5

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model

        return long_name.title()

    def read_odometer(self):
        print("This cat has " + str(self.odometer_reading) + " miles on it.")

    def updata_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            self.odometer_reading = 5

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

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
