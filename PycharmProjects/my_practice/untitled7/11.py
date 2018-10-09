#!/usr/bin/env python3
# -*-coding: utf8-*-
import random
secret = random.randint(1,10)
print(secret)
practise = 0
prac = 1
while True:
    if prac == 0:
        exit()
    temp = input("Please input your number：")
    num = int(temp)
    if num == secret:
        print("You are keara")
        exit()
    else:
        if num < secret:
            print("You are wrong,too small")
            practise = practise + 1
            print(practise)
            prac = 5 - practise
            print(prac)
            print("You have " + str(prac) + "seconds chance")
        else:
            print("You are wrong,too big")
            practise = practise + 1
            print(practise)
            prac = 5 - practise
            print(prac)
            print("You have " + str(prac) + " seconds chance")