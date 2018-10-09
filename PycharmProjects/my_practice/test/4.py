#!/usr/bin/env python3
# -*-coding: utf8-*-
try:
    number = int(input("number: "))
    result = 100 / number
except Exception,e:
    print()
except (ValueError, ZeroDivisionError):
    print ('error:')
except (KeyboardInterrupt, EOFError):
    print ('\nbye-bye')
else:
    print (result)
finally:
    print ('done')
