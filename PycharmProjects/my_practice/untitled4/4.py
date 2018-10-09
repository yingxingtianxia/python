#!/usr/bin/env python3
# -*-coding: utf8-*-
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.tank = 600

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def full_tank(self):
        print("This cat can run " + str(self.tank) + " miles!")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def full_gas_tank(self, trance):
        self.tank = trance

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery")

    def full_gas_tank(self, trance):
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar("telsa", "model s", "2017")
print(my_tesla.get_descriptive_name())
my_tesla.battery_size = 120
my_tesla.describe_battery()
#my_tesla.update_odometer(500)
#my_tesla.read_odometer()
my_tesla.full_gas_tank(400)
my_tesla.full_tank()