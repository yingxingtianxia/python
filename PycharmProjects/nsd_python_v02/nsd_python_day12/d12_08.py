#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import Employees, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

for name, phone in session.query(Employees.name, Employees.phone):
    print(name, '\t', phone)

session.close()
