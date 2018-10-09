#!/usr/bin/env python3
#--coding: utf8--
import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'tedu',
    charset = 'utf8'
)

cur = conn.cursor()
sql4 = "insert into employees(emp_name, genda, phone, dep_id) values(%s, %s, %s, %s)"
data = ('bob', 'male', '15011223344', 3)

result = cur.execute(sql4, data)
print(result)

conn.commit()
cur.close()
conn.close()