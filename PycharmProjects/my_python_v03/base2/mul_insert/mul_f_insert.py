#!/usr/bin/env python3
#__*__coding: utf8__*__
import os
import time
import xlrd
import pymysql
import sys

st = time.time()

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '123456',
    db =  'students',
    charset = 'utf8'
)

cursor = conn.cursor()
sql = 'insert into stu values(%s, %s, %s)'

tb = 'ddl.xlsx'
data = xlrd.open_workbook(tb)
table = data.sheets()[0]
nrows = table.nrows
for i in range(1, nrows):
    value = table.row_values(i)
    dire = value[0]
    try:
        qq = int(str(value[2]).rstrip('.0'))
    except ValueError:
        continue
    ddl = value[2]

    pid = os.fork()
    if not pid:
        cursor.execute(sql, (dire, qq, ddl))
    os.waitpid(-1, 0)

conn.commit()
cursor.close()
conn.close()
et = time.time()
print(et -st)