#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import  Departments, session
from sqlalchemy.orm import aliased

new_dep = aliased(Departments)

for dep_id, dep_name in session.query(new_dep.dep_id,
                                      new_dep.dep_name).\
        order_by(new_dep.dep_id)[1:4]:          #类似于列表
    print(dep_id, '\t', dep_name)

session.close()