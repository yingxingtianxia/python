#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import  Employees, session
from sqlalchemy.orm import aliased

new_emp = aliased(Employees)

query = session.query(new_emp.name, new_emp.phone).order_by(new_emp.emp_id)
print(query)
print()
print(query.all())
print()
print(query.first())
print()

query2 = session.query(new_emp.name, new_emp.phone).filter(new_emp.emp_id == 4)
print(query2.one())
print()
print(query2.scalar())

session.close()