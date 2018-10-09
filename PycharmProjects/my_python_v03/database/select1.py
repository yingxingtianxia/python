#!/usr/bin/env python3
#__*__coding: utf8__*__
from my_python_v03.database.sql_orm import Departments, Empolyees, session

#select * from departments
for instane in session.query(Departments):
    #print(instane)
    print(instane.dep_id , ':' ,instane.dep_name)

#select * from departments order by dep_id
for instane in session.query(Departments).order_by('dep_id'):
    print(instane.dep_id, ':', instane.dep_name)

#select emp_name, phone from employees
for name, phone in session.query(Empolyees.emp_name, Empolyees.phone):
    print('%s: %s' % (name, phone))

