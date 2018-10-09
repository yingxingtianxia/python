#!/usr/bin/env python3
#--*--coding: utf8--*--

class Manufactur():
    def __init__(self, phone, email):
        self.phone = phone
        self.email = email

    def get_phone(self):
        return self.phone

    def update_phone(self, newph):
        self.phone = newph

    def get_email(self):
        return self.email

    def update_email(self, newemail):
        self.email = newemail



class BearToy(object):
    def __init__(self, size, color, phone, email):
        self.size = size
        self.color = color
        self.factory = Manufactur(phone, email)

    def hi(self):
        print('hello world')




if __name__ == '__main__':
    tidy = BearToy('small', 'orange', '12011223344', 'tidy@qq.com')
    print(tidy.factory.get_phone())
    tidy.factory.update_phone('15033445566')
    print(tidy.factory.get_phone())