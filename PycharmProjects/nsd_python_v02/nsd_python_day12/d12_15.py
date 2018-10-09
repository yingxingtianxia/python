#!/usr/bin/env python3
#--coding: utf8--
from sqlalchemy.orm import sessionmaker, aliased
from d12_04 import session, Employees, Departments, Salary
from sqlalchemy import and_, or_

new_emp = aliased(Employees)
#等于
for row in session.query(new_emp.name, new_emp.phone).filter(new_emp.name == 'john'):
    print(row.name, row.phone)
print('#' * 50)
#不等于
for row in session.query(new_emp.name, new_emp.phone).filter(new_emp.name != 'john'):
    print(row.name, row.phone)
print('#' * 50)
#模糊查询
for row in session.query(new_emp.name, new_emp.phone).filter(new_emp.name.like('j%')):
    print(row.name, row.phone)
print('#' * 50)
#并列查询
for row in session.query(new_emp.name, new_emp.phone).filter(new_emp.name.in_(['bob', 'john'])):
    print(row.name, row.phone)
print('#' * 50)
#并列不在
for row in session.query(new_emp.name, new_emp.phone).filter(~new_emp.name.in_(['bob', 'john'])):
    print(row.name, row.phone)
print('#' * 50)
#空
for row in session.query(new_emp.name, new_emp.phone).filter(new_emp.name.is_(None)):
    print(row.name, row.phone)
print('#' * 50)
#非空
for row in session.query(new_emp.name, new_emp.phone).filter(new_emp.name.isnot(None)):
    print(row.name, row.phone)
print('+' * 50)

new_sal = aliased(Salary)
#与
for row in session.query(new_sal.emp_id, new_sal.basic, new_sal.extra).filter(and_(
    new_sal.basic>8000, new_sal.extra>500
)):
    print(row.emp_id)
print('*' * 50)
#或
for row in session.query(new_sal.emp_id, new_sal.basic, new_sal.extra).filter(or_(
    new_sal.basic>8000, new_sal.extra>2000
)):
    print(row.emp_id)
print('*' * 50)

session.close()