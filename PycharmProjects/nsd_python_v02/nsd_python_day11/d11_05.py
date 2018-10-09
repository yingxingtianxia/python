#!/usr/bin/env python3
#--coding: utf8--
import pymysql
import time

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'tedu',
    charset = 'utf8'
)

cur = conn.cursor()
sql5 = "insert into selary(date, emp_id, basic, extra) values (%s, %s, %s, %s)"
data = (time.strftime("%Y-%m-%d"), 1, 10000, 5000)
result = cur.execute(sql5, data)
print(result)
conn.commit()
cur.close()
conn.close()