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

##插入数据

# sql_insert1 = 'insert into departments values (%s, %s)'
# result = cursor.execute(sql_insert1, (7, '行政部'))

# sql_insert2 = 'insert into employees values (%s, %s, %s, %s, %s, %s, %s)'
# employees = [
#     (5, '陈大仙', 'male', '1990-07-23', '15909876543', 'chendaxian@tedu.cn', 2),
#     (6, '张大神', 'male', '1988-01-24', '13888886789', 'zhangdashen@tedu.cn', 3),
#     (7, '林妹妹', 'female', '1992-08-08', '18867896789' , 'linmeimei@tedu.cn', 4),
#     (8, '方小姐', 'female', '1994-09-24', '17710101010', 'fangxiaojie@tedu.cn', 5),
#     (9, '格尔但', 'male', '1987-09-19', '15532322323', 'geerdan@tedu.cn', 6),
#     (10, '阿伊古丽', 'female', '1995-01-01', '18778789898', 'ayiguli@tedu.cn', 7)
# ]
# result = cursor.executemany(sql_insert2, employees)

sql_insert3 = 'insert into departments values (%s, %s)'
result = cursor.execute(sql_insert3, (8, '后勤部'))
#提交结果，写入硬盘
conn.commit()
cursor.close()
conn.close()