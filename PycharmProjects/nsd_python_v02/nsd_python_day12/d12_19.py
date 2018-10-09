#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import Departments, session

dep_yy = Departments(dep_name='yunying')
session.add(dep_yy)

session.commit()
session.close()