#!/usr/bin/env python3
#--coding: utf8--
from d12_01 import Departments, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

dep_dev = Departments(dep_name='developments')
print(dep_dev.dep_name)
print(dep_dev.dep_id)

session.add(dep_dev)
session.commit()
print(dep_dev.dep_id)
session.close()