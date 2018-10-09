#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import Departments, session

for row in session.query(Departments.dep_name.label('部门')):
    print(row.部门)

session.close()