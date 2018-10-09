#!/usr/bin/python
# coding=utf-8

import mysql.connector

config = {
    'host': '192.168.99.100',
    'port': 43306,
    'database': 'test',
    'user': 'happy',
    'password': 'happy',
    'charset': 'utf8',
    'use_unicode': True,
    'get_warnings': True,
}
db = mysql.connector.Connect(**config)
cursor = db.cursor()
sql = "SELECT * FROM student"
cursor.execute(sql)

for row in cursor.fetchall():
    print(row[0],row[1],row[2])

cursor.close()
db.close()
