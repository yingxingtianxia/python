#!/usr/bin/env python3
#__*__coding: utf8__*__
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:123456@localhost/tedu?charset=utf8',
    encoding = 'utf8',
    echo = False
)

Session = sessionmaker()
session = Session(bind=engine)

sql1 = 'show databases;'
res1 = session.execute(sql1).fetchall()
print(res1)

sql2 = 'use tedu;'
res2 = session.execute(sql2)
print(res2)

sql3 = 'show tables;'
res3 = session.execute(sql3).fetchall()
print(res3)

sql4 = 'select * from %s' % res3[1][0]
res4 = session.execute(sql4)
print(res4)