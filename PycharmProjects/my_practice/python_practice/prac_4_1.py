#!/usr/bin/env python
#--coding: utf8--
import datetime

date = raw_input('请输入日期（格式是年月日/20170101）：')
year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:8])
print '你输入的日期是%d年%d月%d日' % (year, month, day)

targetDay = datetime.date(year, month, day)
dayCount = targetDay - datetime.date(targetDay.year - 1, 12, 31)        #减去上一年的最后一天
days = dayCount.days
print '%s是%s年的第%s天' % (date, year, days)