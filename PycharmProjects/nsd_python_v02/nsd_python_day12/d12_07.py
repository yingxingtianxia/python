#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import engine, Departments
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

for instance in session.query(Departments).order_by(Departments.dep_id):
    print(instance.dep_id, '\t', instance.dep_name)

session.close()