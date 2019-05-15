#!/usr/bin/env python3
import sys
from datetime import datetime
from datetime import timedelta


# date = input('请输入启始日期（格式为YYYY-MM-DD）:')
def count_date(date,days):
    #print(date)
    date_list = date.split('-')

    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])

    if year not in range(1000,10000):
        print('年份有误')
        sys.exit(1)

    if month not  in range(1,13):
        print('月份有误')
        sys.exit(1)

    if year % 4 == 0 and year %100 != 0:
        if month in [1,3,5,7,8,10,12]:
            if day not in range(1,32):
                print('日期有误')
                sys.exit(1)
        elif month in [4,6,9,11]:
            if day not in range(1,31):
                print('day error')
                sys.exit(1)
        else:
            if day not in range(1,30):
                print('日期有误')
                sys.exit(1)
    else:
        if month in [1,3,5,7,8,10,12]:
            if day not in range(1,32):
                print('day error')
                sys.exit(1)
        elif month in [4,6,9,11]:
            if day not in range(1,31):
                print('day error')
                sys.exit(1)
        else:
            if day not in range(1,29):
                print('day error')
                sys.exit(1)

    # print(type(date))
    d = datetime.strptime(date,'%Y-%m-%d')
    # print(d)
    # print(type(d))

    delta = timedelta(days=days)
    n_days_after = d + delta
    n_days_before = d - delta

    d_list = [n_days_before.strftime('%Y-%m-%d'), n_days_after.strftime('%Y-%m-%d')]
    # print(n_day_after.strftime('%Y-%m-%d'))

    return d_list

if __name__ == '__main__':
    date = input('请输入启始日期（格式为YYYY-MM-DD）:')
    days = int(input('请输入跨越天数：'))
    d = count_date(date,days)
    print('当前输入的日期是%s' % date)
    print('前推%s天的日期是%s' % (days,d[0]))
    print('后推%s天的日期是%s' % (days,d[1]))

