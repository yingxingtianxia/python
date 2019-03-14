#!/usr/bin/env python3
import xlwt

users = [['username','password','uid','gid','desc','homedir','shell'],]
with open('passwd', 'r') as fobj:
    data = fobj.readlines()
    for i in data:
        i = i.split(':')
        i[6] = i[6].strip('\n')
        users.append(i)

book = xlwt.Workbook()
sheet = book.add_sheet('user')

row = 1

for user in users:
    col = 0
    for u in user:
        sheet.write(row,col,u)
        col += 1
    row += 1

book.save('user.xlsx')