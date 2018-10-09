#!/usr/bin/env python3
# -*-coding: utf8-*-
def game():
    import random
    print("I have a number")
    com = random.randint(1,100)
    while True:
        per = int(input("a number: "))
        if per == com:
            print("yes")
            exit()
        elif per > com:
            print("big")
        else:
            print("small")


game()
