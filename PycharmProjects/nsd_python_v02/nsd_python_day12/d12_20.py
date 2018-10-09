#!/usr/bin/env python3
#--coding: utf8--
#更新字段的时候不能用别名
from d12_04 import Departments, session

query = session.query(Departments).filter(Departments.dep_id == 8)
query.update({Departments.dep_name:'运营'})

session.commit()
session.close()