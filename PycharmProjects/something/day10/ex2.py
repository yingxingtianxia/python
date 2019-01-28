#!/usr/bin/env python3
import xlwt


stus = [['姓名', '年龄'],['张三','20']]

book = xlwt.Workbook()
sheet = book.add_sheet('student')

row = 0
for stu in stus:
    col = 0
    for s in stu:
        sheet.write(row,col,s)
        col += 1
    row += 1
book.save('stu.xlsx')


















users = [['用户名','密码站位符','uid','gid','描述信息','用户家目录','shell'],]
with open('passwd', 'r') as fobj:
    data = fobj.readlines()
    for i in data:
        i = i.split(':')
        i[6] = i[6].strip('\n')
        users.append(i)


book = xlwt.Workbook()
sheet = book.add_sheet('user')

row = 0

for user in users:
    col = 0
    for u in user:
        sheet.write(row,col,u)
        col += 1
    row += 1

book.save('stus.xlsx')

