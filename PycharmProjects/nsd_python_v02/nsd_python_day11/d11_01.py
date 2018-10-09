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
sql1 = "insert into departments(dep_name) values(%s)"
result = cur.execute(sql1, ('development',))
print(result)
conn.commit()
cur.close()
conn.close()