#!/usr/bin/env python3
#__*__coding: utf8__*__
import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '123456',
    db = 'tarena',
    charset = 'utf8'
)

cursor = conn.cursor()

sql_select1 = 'select * from departments order by dep_id'
cursor.execute(sql_select1)

result1 = cursor.fetchone()
print(result1)

result2 = cursor.fetchmany(2)
print(result2)

result3 = cursor.fetchall()
print(result3)

cursor.close()
conn.close()