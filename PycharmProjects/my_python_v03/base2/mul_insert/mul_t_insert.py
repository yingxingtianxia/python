#!/usr/bin/env python3
#__*__coding: utf8__*__
import xlrd
import threading
import time
import pymysql

st = time.time()

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '123456',
    db = 'students',
    charset = 'utf8'
)

cursor = conn.cursor()
sql = 'insert into stu values (%s, %s, %s)'

def insert_data(dire, qq, ddl):
    cursor.execute(sql, (dire, qq, ddl))
    return 'done'

tb = 'ddl.xlsx'
data = xlrd.open_workbook(tb)
table = data.sheets()[0]
nrows = table.nrows
for i in range(1, nrows):
    value = table.row_values(i)
    dire = value[0]
    try:
        qq = int(str(value[1]).rstrip('.0'))
    except ValueError:
        continue
    ddl = value[2]

    t = threading.Thread(target=insert_data, args=(dire, qq, ddl))
    t.start()

conn.commit()
cursor.close()
conn.close()
et = time.time()
print(et-st)
