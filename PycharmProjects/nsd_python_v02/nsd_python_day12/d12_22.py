#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import Departments, session

dep_yy = session.query(Departments).get(8)
session.delete(dep_yy)

session.commit()
session.close()