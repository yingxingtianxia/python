#!/usr/bin/env python3
#__*__coding: utf8__*__
from my_python_v03.database.sql_orm import Departments, Empolyees, Salary, session

#select * from departments order by dep_id limit 1, 3
for row in session.query(Departments).order_by(Departments.dep_id)[1:4]:
    print(row.dep_id, ':', row.dep_name)

#select * from departments where dep_id = 2
for row in session.query(Departments).filter(Departments.dep_id==2):
    print(row.dep_id, ':', row.dep_name)
for row in session.query(Departments).filter(Departments.dep_id>2):
    print(row.dep_id, ':', row.dep_name)
for row in session.query(Departments).filter(Departments.dep_id>2).order_by(Departments.dep_id.desc()):
    print(row.dep_id, ':', row.dep_name)
for row in session.query(Departments).order_by(Departments.dep_id.desc()).filter(Departments.dep_id>2):
    print(row.dep_id, ':', row.dep_name)

#select emp_id, basic, award from salary where date='2018-09-05' and award>2000
for row in session.query(Salary).filter(Salary.date=='2018-09-05').filter(Salary.award>2000):
    print(row.emp_id, row.basic, row.award)
#select emp_id basic,award from salary where date='2018-09-05' and award>2000 and basic>10000
for row in session.query(Salary).filter(Salary.date=='2018-09-05').filter(Salary.award>2000).filter(Salary.basic>10000):
    print(row.emp_id, row.basic, row.award)

#select emp_name from employees where emp_name like '王%'
#在sql语句中，模糊查询用法中%表示多个字符，_表示一个字符
for row in session.query(Empolyees).filter(Empolyees.emp_name.like('王%')):
    print(row.emp_name)
for row in session.query(Empolyees).filter(Empolyees.emp_name.like('王___')):
    print(row.emp_name)
