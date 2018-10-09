#!/usr/bin/env python3
#__*__coding: utf8__*__
from my_python_v03.database.sql_orm import Empolyees, session

#all()返回的列表
res1 = session.query(Empolyees.emp_name, Empolyees.phone).all()
print(res1)

#first()返回第一条记录
res2 = session.query(Empolyees.emp_name).filter(Empolyees.emp_name.like('王%')).first()
print(res2)

#one()要求查询结果只能有一条记录
res3 = session.query(Empolyees.emp_name).filter(Empolyees.emp_name.like('林%')).one()
print(res3)
#如果返回结果不是一行，则报错multiple rows were found for one()
# res4 = session.query(Empolyees.emp_name).filter(Empolyees.emp_name.like('王%')).one()
# print(res4)

#scalar调用one，只返回第一列
res5 = session.query(Empolyees.emp_name, Empolyees.phone, Empolyees.email).filter(
    Empolyees.emp_name.like('林%')).one()
print(res5)
res6 = session.query(Empolyees.emp_name, Empolyees.phone, Empolyees.email).filter(
    Empolyees.emp_name.like('林%')).scalar()
print(res6)