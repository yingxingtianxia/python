#!/usr/bin/env python
#--coding: utf8--
class AddrBook(object):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_phone(self):
        return self.phone

    def update_phone(self, newph):
        self.phone = newph
        print '%s update phone number: %s' % (self.name, self.phone)

if __name__ == '__main__':
    bob = AddrBook('Bob Green', '13311223344')
    alice = AddrBook('Alice Smith', '13377889900')
    print bob.get_phone()
    bob.update_phone('18811112222')