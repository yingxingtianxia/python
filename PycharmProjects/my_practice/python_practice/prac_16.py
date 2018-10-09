#!/usr/bin/env python
#--coding: utf8--
import time
print time.time()
print time.strftime('%Y%m%d')
print time.strftime('%H:%M:%S')
print time.localtime()
print time.strftime('%j')


import datetime

print datetime.date.today() #datetime.date(2017, 6, 27)
print datetime.date.today().strftime('%d/%m/%Y') #'27/06/2017'
print datetime.date(1941, 1, 5) #datetime.date(1941, 1, 5)