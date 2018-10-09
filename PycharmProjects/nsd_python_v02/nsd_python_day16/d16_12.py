#!/usr/bin/env python3
#--*--coding: utf8--*--
from mysql import connector

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'flask',
    'user': 'happy',
    'password': 'happy',
    'charset': 'utf8',
    'use_unicode': True,
    'get_warnings': True,
}

db = connector.Connect(**config)
cursor = db.cursor()
sql = 'select * from student'
cursor.execute(sql)

for row in cursor.fetchall():
    print(row[0], '\t', row[1], '\t', row[2])

cursor.close()
db.close()