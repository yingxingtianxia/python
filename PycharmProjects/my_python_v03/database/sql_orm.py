#!/usr/bin/env python3
#__*__coding: utf8__*__
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine = create_engine(
    'mysql+pymysql://root:123456@localhost/tedu?charset=utf8',
    encoding = 'utf8',
    #echo = True
)
#创建sqlalchemy的表的基类，创建表时可直接继承这个类
Base = declarative_base()
#创建session，直接绑定到engine
Session = sessionmaker()
session = Session(bind=engine)

#表一旦创建，无法再通过代码修改表结构，需要把表删除，然后重新执行
class Departments(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer, primary_key=True, autoincrement=True)
    dep_name = Column(String(20), unique=True)
    def __str__(self):
        return '<Departments(dep_name=%s)>' % self.dep_name


class Empolyees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20), nullable=False)
    gender = Column(Enum('male', 'female'), nullable=False)
    phone = Column(String(11), unique=True, nullable=False)
    email = Column(String(40), unique=True)
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))
    def __str__(self):
        return '<Employees(emp_name=%s)>' % self.emp_name


class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer, nullable=False)
    award = Column(Integer)
    def __str__(self):
        return '<Salary(date=%s>' % self.date



if __name__ == '__main__':
    Base.metadata.create_all(engine)