#!/usr/bin/env python3
#__*__coding: utf8__*__
from sqlalchemy_conn import Departments
from sqlalchemy_conn import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
session = Session(bind=engine)

hr = Departments(dep_name='人事部')
dev = Departments(dep_name='开发部')
ops = Departments(dep_name='运维部')
# print(hr)
# print(hr.dep_id)
# print(hr.dep_name)

##将需要插入的数据添加到session
#提交单个条目
#session.add(hr)
#提交多个条目
session.add_all([hr, dev, ops])

#提交动作，执行硬盘读写，将数据写入表中
session.commit()
session.close()
