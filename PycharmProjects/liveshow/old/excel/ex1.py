#!/usr/bin/env python3
import xlrd

data = xlrd.open_workbook('grade.xlsx')

tables = data.sheets()
#print(tables)

# for i in range(len(tables)):
#     table = tables[i]
#     nrows = table.nrows
#     print('%s表有%s行' % (table.name,nrows))

for i in range(len(tables)):
    table = tables[i]
    nrows = table.nrows
    values = table.row_values
    #print(nrows,values)
    for j in range(2,nrows):
        value = values(j)
        value[0] = int(value[0])
        value[2] = int(value[2])
        print(value)