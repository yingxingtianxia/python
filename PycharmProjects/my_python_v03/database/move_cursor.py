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

sql = 'select * from departments order by dep_id'
cursor.execute(sql)
# cursor.scroll(3, mode='absolute')
# res = cursor.fetchmany(8)
#res = cursor.fetchall()
cursor.fetchone()
#cursor.scroll(3, mode='relative')
cursor.scroll(3, mode='absolute')
res = cursor.fetchmany(2)
print(res)