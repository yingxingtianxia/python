#!/usr/bin/env python3
# -*-coding: utf8-*-
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
my_new_car = Car("buick", "excellt", "2017")
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
print()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print()
my_new_car.updata_odometer(3)
my_new_car.read_odometer()
print()
#my_new_car.increment_odometer(100)
#my_new_car.read_odometer()
my_new_car.increment_odometer(-5)
my_new_car.read_odometer()
