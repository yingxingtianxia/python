#!/usr/bin/env python3
# -*-coding: utf8-*-
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number = 0

    def describe_restaurant(self):
        print(self.name.title() + "'s type is " +self.type + ".")

    def open_restaurant(self):
        print(self.name + " is opening now.")

    def set_number(self, number):
        self.number += number

my_restauant = Restaurant("waiting bar", "drunk")
#zhangsan_restaurant = Restaurant("dayali", "kaoya")
#lisi_restaurant = Restaurant("donglaishun", "shuanyangrou")
print("My restaurant's name is " + my_restauant.name + ".")
print("My restaurant's type is " + my_restauant.type + ".")
print("")
my_restauant.describe_restaurant()
my_restauant.open_restaurant()
#print()
#zhangsan_restaurant.describe_restaurant()
#print()
#lisi_restaurant.describe_restaurant()
#my_restauant.number = 500
#print("There are " + str(my_restauant.number) + " pepple have dinner ate here")
my_restauant.set_number(50)
print("There are " + str(my_restauant.number) + " pepple have dinner ate here")
my_restauant.set_number(50)
print("There are " + str(my_restauant.number) + " pepple have dinner ate here")