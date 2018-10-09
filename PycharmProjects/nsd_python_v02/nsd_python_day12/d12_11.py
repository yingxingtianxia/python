#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import Employees, session
from sqlalchemy.orm import aliased

new_emp = aliased(Employees)

for name, phone in session.query(new_emp.name, new_emp.phone):
    print(name, phone)

session.close()