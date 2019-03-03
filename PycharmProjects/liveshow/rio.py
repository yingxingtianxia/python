#!/usr/bin/env python3
import pymysql
from datetime import datetime

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '123456',
    db = 'testdb',
    charset = 'utf8'
)

cursor = conn.cursor()

q1_sql = 'select curdate()'
q2_sql = 'select * from myapp_message'

cursor.execute(q1_sql)
n_day = cursor.fetchone()[0]
print(n_day)






# cursor.execute(q1_sql)
# for item in cursor.fetchall():
#     print(item)

cursor.close()
conn.close()