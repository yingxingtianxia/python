#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import Salary, engine
from sqlalchemy.orm import sessionmaker
from datetime import date

Session = sessionmaker(bind=engine)
session = Session()

date1 = date(2018, 1, 1)
date2 = date(2018, 2, 1)

bob1 = Salary(date=date1, emp_id=1, basic=10000, extra=5000)
bob2 = Salary(date=date2, emp_id=1, basic=10000, extra=6000)
alice1 = Salary(date=date1, emp_id=2, basic=4000, extra=3000)
alice2 = Salary(date=date2, emp_id=2, basic=4000, extra=3500)
john1 = Salary(date=date1, emp_id=3, basic=8000, extra=1000)
john2 = Salary(date=date2, emp_id=3, basic=8000, extra=500)
jack1 = Salary(date=date1, emp_id=4, basic=6000, extra=2000)
jack2 = Salary(date=date2, emp_id=4, basic=6000, extra=1500)

session.add_all([bob1, bob2, alice1, alice2, john1, john2, jack1, jack2])
session.commit()
session.close()