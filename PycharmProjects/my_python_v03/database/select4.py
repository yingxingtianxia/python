#!/usr/bin/env python3
#__*__coding: utf8__*__
from my_python_v03.database.sql_orm import Empolyees, session

#select emp_name from employees where emp_name=='张三' and where emp_name=='李四'
#select emp_name from employees where emp_name in ('张三', '李四')
for row in session.query(Empolyees).filter(Empolyees.emp_name.in_(['张三', '李四'])):
    print(row.emp_name)

#select emp_name from employees where emp_name not in ('张三', '李四')
for row in session.query(Empolyees).filter(~Empolyees.emp_name.in_(['张三', '李四'])):
    print(row.emp_name)

#select emp_name from employess where emp_name is not null
for row in session.query(Empolyees).filter(Empolyees.emp_name.isnot(None)):
    print(row)