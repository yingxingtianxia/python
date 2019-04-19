#!/usr/bin/env python3
import time
import subprocess

com1 = 'mysql -uroot -p123456 tedu -e "select ts from password order by id DESC limit 1" | tail -1'

sql_time = subprocess.getoutput(com1)
s_time = int(time.mktime(time.strptime(sql_time,"%Y-%m-%d %H:%M:%S")))

now_time = int(time.time())

r_time = now_time - s_time

if r_time >= 1800:
    print('yes')
else:
    print('no')