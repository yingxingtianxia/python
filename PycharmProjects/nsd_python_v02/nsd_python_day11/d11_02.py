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
sql2 = "insert into departments(dep_name) values (%s)"

data = [('hr',), ('ope',)]
result = cur.executemany(sql2, data)
print(result)

conn.commit()
cur.close()
conn.close()