#!/usr/bin/env python
#--coding: utf8--
class Hotel():
    def __init__(self, room, cf=1.0, br=15):
        self.room = room
        self.cf = cf
        self.br = br

    def calc_all(self, days=1):
        return (self.room * self.cf + self.br) * days

if __name__ == '__main__':
    stdroom = Hotel(200)
    print stdroom.calc_all()
    print stdroom.calc_all(2)
    bigbed = Hotel(300, 0.9)
    print bigbed.calc_all()
    print bigbed.calc_all(5)