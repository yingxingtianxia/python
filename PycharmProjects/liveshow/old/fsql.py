#!/usr/bin/env python3
import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '123456',
    db = 'tedu',
    charset = 'utf8'
)

cursor = conn.cursor()

table_create = 'create table password (id int(2) auto_increment primary key,\
                username varchar(20),\
                placeholder char(5),\
                uid int(2),\
                gid int(2),\
                description varchar(100),\
                homedir varchar(50),\
                shell char(20),\
                index(username)\
                )'
table_show = 'show tables;'
table_dt = 'drop table password'
sql_in = 'insert into password(username,placeholder,uid,gid,description,homedir,shell) values(%s,%s,%s,%s,%s,%s,%s)'
sql_se = 'select * from password'


cursor.execute(table_show)
if ('password') in cursor.fetchall():
    print('表以存在')
    cursor.execute(table_dt)
    print('表以删除')

try:
    cursor.execute(table_create)
except pymysql.err.InternalError:
    print('表以存在')
except pymysql.err.ProgrammingError:
    print('sql语句有误')
else:
    print('建表成功')

with open('/etc/passwd', 'r') as fobj:
    for item in fobj:
        username,placeholder,uid,gid,description,homedir,shell = item.split(':')
        cursor.execute(sql_in,(username,placeholder,uid,gid,description,homedir,shell.rstrip('\n')))


conn.commit()

cursor.execute(sql_se)
for item in cursor.fetchall():
    print(item)

cursor.close()
conn.close()
