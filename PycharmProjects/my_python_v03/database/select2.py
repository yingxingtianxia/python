#!/usr/bin/env python3
#__*__coding: utf8__*__
from my_python_v03.database.sql_orm import Departments, session

#selct dep_id, dep_name from departments
for row in session.query(Departments.dep_id, Departments.dep_name):
    print(row)

for row in session.query(Departments, Departments.dep_name):
    print(row.dep_name)

for row in session.query(Departments, Departments.dep_id, Departments.dep_name):
    print(row.dep_id, row.dep_name)

for row in session.query(Departments.dep_name.label('部门')):
    print(row.部门)

for row in session.query(Departments.dep_name).order_by('dep_id'):
    print(row)

for row in session.query(Departments).order_by(Departments.dep_id):
    print(row.dep_id,':', row.dep_name)

for row in session.query(Departments).order_by(Departments.dep_id.desc()):
    print(row.dep_id,":",row.dep_name)