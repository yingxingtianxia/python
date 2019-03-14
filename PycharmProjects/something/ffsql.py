#!/usr/bin/env python3
import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password ='123456',
    db = 'tedu',
    charset = 'utf8'
)
cursor = conn.cursor()

se1 = "select max(id) from password"

res1 = cursor.execute(se1)
mid = cursor.fetchone()[0]

se2 = "select ts from password where id = %s" % mid
cursor.execute(se2)
res2 = cursor.fetchone()
print(res2)

cursor.close()
conn.close()