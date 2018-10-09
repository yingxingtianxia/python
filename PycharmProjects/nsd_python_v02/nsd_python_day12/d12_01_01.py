#!/usr/bin/env python3
#--coding: utf8--
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(
    'mysql+pymysql://root:123456@localhost/tarena?charset=utf8',
    encoding = 'utf8',
    echo = True
)

Base = declarative_base()

class Departments(Base):
    __tablename__ = 'departments'

    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20))

    def __repr__(self):
        return "<Departments(dep_name=%s)>" % self.dep_name

if __name__ == '__main__':
    Base.metadata.create_all(engine)