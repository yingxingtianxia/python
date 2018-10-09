#!/usr/bin/env python3
#__*__coding: utf8__*__
from my_python_v03.database.sql_orm import Salary, session
from sqlalchemy import and_, or_

#select * from salary where award>2000 and basic>10000
for row in session.query(Salary).filter(
    and_(Salary.basic>10000, Salary.award>2000)
).filter(Salary.date=='2018-09-05'):
    print(row.emp_id, row.basic, row.award)

#select * from salary where award>2000 or basic>10000
for row in session.query(Salary).filter(
    or_(Salary.basic>10000, Salary.award>2000)
).filter(Salary.date=='2018-09-05'):
    print(row.emp_id, row.basic, row.award)