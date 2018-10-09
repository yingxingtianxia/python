#!/usr/bin/env python3
#__*__coding: utf8__*__
from my_python_v03.database.sql_orm import Departments, Empolyees, Salary, session

#select count(*) from employees
emp_count = session.query(Empolyees).count()
print(emp_count)

#多表查询
#select e.emp_name, d.dep_name from employees as e join departments as d on e.dep_id=d.dep_id
# for name, department in session.query(
#     Empolyees.emp_name, Departments.dep_name
# ).join(Departments, Empolyees.dep_id==Departments.dep_id):
#     print(name, department)
res = session.query(Empolyees.emp_name, Departments.dep_name).join(
    Departments, Empolyees.dep_id==Departments.dep_id).all()
print(res)

result = session.query(Empolyees.emp_name, Salary.basic+Salary.award).filter(
    Salary.date=='2018-09-05').join(
    Salary, Empolyees.emp_id==Salary.emp_id).all()
for name, salary in result:
    print(name, salary)

resu = session.query(Empolyees.emp_name, Departments.dep_name, Salary.basic+Salary.award).filter(
    Salary.date=='2018-09-05').join(
    Departments, Empolyees.dep_id==Departments.dep_id).join(
    Salary, Empolyees.emp_id==Salary.emp_id).all()
for name, dep, salary in resu:
    print(name, dep, salary)