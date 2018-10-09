#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import Employees, session
from sqlalchemy.orm import aliased

new_dep = aliased(Employees)

result = {}
for name, phone in session.query(new_dep.name, new_dep.phone).\
    filter(new_dep.dep_id == 5):
    result[name] = phone
print(result)

session.close()