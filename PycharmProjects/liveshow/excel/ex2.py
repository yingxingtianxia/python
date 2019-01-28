#!/usr/bin/env python3
import xlwt

stus = [['姓名','年龄'],['张三','20']]

book = xlwt.Workbook()
sheet = book.add_sheet('student')

row = 5
for stu in stus:
    col = 5
    for s in stu:
        sheet.write(row,col,s)
        col += 1
    row += 1

book.save('stu.xlsx')