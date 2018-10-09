#!/usr/bin/env python3
#--*--coding: utf8--*--
class BearToy():
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def sing(self, song):
        print(song)


class NewBearToy(BearToy):
    def run(self):
        print('I can run')

if __name__ == '__main__':
    b1 = NewBearToy('middle', 'green')
    b1.sing('hahaha...')
    b1.run()

    b2 = BearToy('large', 'white')
    b2.sing('wowowo....')