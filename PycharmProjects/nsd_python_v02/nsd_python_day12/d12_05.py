#!/usr/bin/env python3
#--coding: utf8--
from d12_04 import Employees, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

bob = Employees(name='bob', genda='male', phone='13312345678', dep_id=1)
alice = Employees(name='alice', genda='female', phone='15011223344', dep_id=4)
john = Employees(name='john', genda='male', phone='18633334444', dep_id=5)
jack = Employees(name='jack', genda='male', phone='15655556666', dep_id=5)

session.add_all([bob, alice, john, jack])
session.commit()
session.close()