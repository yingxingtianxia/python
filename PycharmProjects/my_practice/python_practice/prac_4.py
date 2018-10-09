#!/usr/bin/env python
#--coding: utf8--
import sys

date = raw_input('请输入日期（格式是年月日/20170101）：')
year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:8])
print '你输入的日期是%d年%d月%d日' % (year, month, day)

b_m = [1, 3, 5, 7, 8, 10, 12]
s_m = [4, 6, 9, 11]

if year % 4 == 0:
    if (month == 2 and day > 29) or (month in b_m and day > 31) or (month in s_m and day > 30):
        print '日期有错'
        sys.exit()
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    if (month == 2 and day > 28) or (month in b_m and day > 31) or (month in s_m and day > 30):
        print '日期有错'
        sys.exit()
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m_ds = 0
for i in range(1,13):
    if i == month:
        for j in range(i-1):
            m_ds+= months[j]
        days = m_ds + day

print '%s是%s年的第%s天' % (date, year, days)