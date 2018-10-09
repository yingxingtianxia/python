#!/usr/bin/env python
#--coding: utf8--
class UserInfo(object):
    def __init__(self, phone, email):
        self.phone = phone
        self.email = email

    def get_phone(self):
        return self.phone

    def update_phone(self, newph):
        self.phone = newph
        #print '%s update phone number: %s' %  (self.name, self.phone)

    def get_email(self):
        return self.email

    def update_email(self, newemail):
        self.email = newemail

class AddrBook(object):
    def __init__(self, name, phone, email):
        self.name = name
        self.info = UserInfo(phone, email)

if __name__ == '__main__':
    bob = AddrBook('Bob Green', '13312341234', 'bob@tedu.cn')
    print bob.info.get_phone()
    print bob.info.get_email()
    bob.info.update_phone('15555555555')
    print bob.info.get_phone()
    bob.info.update_email('bob@tarena.com')
    print bob.info.get_email()