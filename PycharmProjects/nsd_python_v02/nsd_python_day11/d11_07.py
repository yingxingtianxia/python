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
sql6 = "select dep_id, dep_name from departments"
cur.execute(sql6)
result = cur.fetchone()
print(result)
result2 = cur.fetchmany(2)
print(result2)
cur.close()
conn.close()