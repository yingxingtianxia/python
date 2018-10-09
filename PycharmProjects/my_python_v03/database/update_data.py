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

sql = 'update departments set dep_name="后勤部" where dep_name="后勤保障部"'
res = cursor.execute(sql)
print(res)
conn.commit()

cursor.close()
conn.close()