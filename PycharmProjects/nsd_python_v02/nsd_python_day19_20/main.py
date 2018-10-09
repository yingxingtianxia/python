#!/usr/bin/env python3
#--*--coding: utf8--*--
import reader as input
import mycal as cal

i = 0
while True:
    log = input.read()
    if log == None:
        break
    cal.cal(log)
    i = i+1
    print(i, log['sdate'])

print(cal.act_count)