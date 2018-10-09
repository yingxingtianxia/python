#!/usr/bin/env python3
#--coding: utf8--
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'mysql+pymysql://root:123456@localhost/tarena?charset=utf8',
    encoding = 'utf8',
    #echo = True
)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Departments(Base):
    __tablename__ = 'departments'

    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20))

    def __repr__(self):
        return "<Departments(dep_name=%s)>" % self.dep_name

class Employees(Base):
    __tablename__ = 'employees'

    emp_id = Column(Integer, primary_key=True)
    name = Column(String(20))
    genda = Column(String(10))
    phone = Column(String(11))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __repr__(self):
        return "<Employee(name=%s)>" % self.name

class Salary(Base):
    __tablename__ = 'salary'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    extra = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)