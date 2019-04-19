#!/usr/bin/env python3
#__*__coding: utf8__*__
import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '123456',
    db = 'live',
    charset = 'utf8'
)

cursor = conn.cursor()

sql_ct = 'create table password (\
          id int(2) auto_increment primary key, \
          username char(20),\
          placeholder char(5),\
          uid int(2),\
          gid int(2),\
          description char(80),\
          homedir char(25),\
          shell char(20),\
          index(username)\
          );'

sql_show = 'show tables;'
sql_dt = 'drop table password;'
sql_in = 'insert into password(username,placeholder,uid,gid,description,homedir,\
          shell) values(%s,%s,%s,%s,%s,%s,%s)'
sql_se = 'select * from password'


cursor.execute(sql_show)
if ('password',) in cursor.fetchall():
    print('表以存在')
    cursor.execute(sql_dt)
    print('删除以存在表')

try:
    cursor.execute(sql_ct)
except pymysql.err.InternalError:
    print('表以存在')
except pymysql.err.ProgrammingError:
    print('sql语句语法错误')
else:
    print('建表成功')

with open('passwd') as fobj:
    for item in fobj:
        username,placeholder,uid,gid,description,homedir,shell = item.split(':')
        cursor.execute(sql_in,(username,placeholder,uid,gid,description,homedir,shell.rstrip('\n')))
conn.commit()

cursor.execute(sql_se)
for item in cursor.fetchall():
    print(item)
cursor.close()
conn.close()