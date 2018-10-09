#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import Departments, session

for row in session.query(Departments, Departments.dep_name):
    print(row.Departments, row.dep_name)

session.close()