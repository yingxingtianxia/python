#!/usr/bin/env python3
#--coding: utf8--
from sqlalchemy.orm import aliased
from d12_04 import Employees, session

new_emp = aliased(Employees)

query = session.query(new_emp).filter(new_emp.dep_id == 5)
print(query.count())