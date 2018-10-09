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
sql10 = "update departments set dep_name=%s where dep_name=%s"
result = cur.execute(sql10, ('operations', 'ope'))
print(result)
conn.commit()
cur.close()
conn.close()