#!/usr/bin/env python3
#--coding: utf8--
from sqlalchemy.orm import  aliased
from d12_04 import Departments, session, Employees

new_emp = aliased(Employees)
new_dep = aliased(Departments)

query = session.query(new_emp.name, new_dep.dep_name).join(new_dep, new_emp.dep_id == new_dep.dep_id)
print(query.all())