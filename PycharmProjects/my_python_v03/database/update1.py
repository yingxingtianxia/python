#!/usr/bin/env python3
#__*__coding: utf8__*__
from my_python_v03.database.sql_orm import Departments, session

q = session.query(Departments).filter(Departments.dep_name=='人事部')
q.update({Departments.dep_name: '人力资源部'})
session.commit()
session.close()
