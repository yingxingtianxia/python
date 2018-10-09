#!/usr/bin/env python3
#__*__coding: utf8__*__
from my_python_v03.database.sql_orm import Departments, session

q = session.query(Departments).get(1)
q.dep_name = 'HR'
session.commit()
session.close()