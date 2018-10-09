#!/usr/bin/env python3
#--coding: utf8--
from d12_01_01 import Departments, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

dep_hr = Departments(dep_name='hr')
dep_op = Departments(dep_name='operations')
dep_finance = Departments(dep_name='财务')
dep_xz = Departments(dep_name='行政')

session.add_all([dep_hr, dep_op, dep_finance, dep_xz])
session.commit()
session.close()