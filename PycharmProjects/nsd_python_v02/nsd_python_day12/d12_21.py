#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import Departments, session

dep_yy = session.query(Departments).get(8)
print(dep_yy)
dep_yy.dep_name = '运营部'

session.commit()
session.close()