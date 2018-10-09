#!/usr/bin/env python
#--coding: utf8--
import d8_03

class EmplAddrBook(d8_03.AddrBook):
    def __init__(self, name, phone, email):
        #d8_03.AddrBook.__init__(self, name, phone)
        super(EmplAddrBook, self).__init__(name, phone)
        self.email = email

    def get_email(self):
        return self.email

if __name__ == '__main__':
    tom = EmplAddrBook('Tom Kbofier', '15099887766', 'tom@163.com')
    print tom.get_phone()
    tom.update_phone('18833334444')
    print tom.get_email()