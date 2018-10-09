#!/usr/bin/env python3
#--*--coding: utf8--*--
class Date():
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    @classmethod
    def create_date(cls, string_date):
        year, month, date = map(int, string_date.split('-'))
        dt = cls(year, month, date)
        return dt

    @staticmethod
    def is_date_valid(sting_date):
        year, month, date = map(int, sting_date.split('-'))
        return year < 4000 and 0 < month <13 and 0 < date < 32


if __name__ == '__main__':
    d1 = Date(2018, 8, 17)
    d2 = Date.create_date('2020-04-22')
    print(d2.year, d2.month, d2.date)
    print(Date.is_date_valid('2022-22-4'))

    if Date.is_date_valid('2020-10-4'):
        d3 = Date.create_date('2020-10-4')
        print('create instance done')
    else:
        print('Invalid date format.')