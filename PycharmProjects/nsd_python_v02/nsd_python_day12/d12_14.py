#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import  Salary, session
from sqlalchemy.orm import  aliased

new_sal = aliased(Salary)
for empid in session.query(new_sal.emp_id).filter(new_sal.basic>8000).filter(new_sal.extra>1000):
    print(empid)

session.close()