#!/usr/bin/env python3
import pymysql
import time

conn = pymysql.connect(
    host = '192.168.4.1',
    user = 'root',
    password = '123456',
    db = 'mydb',
    port = 3306,
    charset = 'utf8'
)

cursor = conn.cursor()

sql_insert = 'insert into stu values (%s)'

for i in range(1000):
    cursor.execute(sql_insert, (int(i)))
    conn.commit()
    time.sleep(1)

cursor.close()
conn.close()