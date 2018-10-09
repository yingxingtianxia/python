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
sql = "insert into student value(44,'John',44);"
cursor.execute(sql)
db.commit()
cursor.close()
db.close()
