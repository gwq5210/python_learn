#!/usr/bin/env python
# coding=utf-8

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
	__tablename__ = 'user'
	id = Column(String(20), primary_key = True)
	name = Column(String(20))
engine = create_engine('mysql+mysqlconnector://root:1234@localhost:3306/gwq')
DBSession = sessionmaker(bind = engine)
session = DBSession()
new_user = User(id = '5', name = 'cx')
session.add(new_user)
session.commit()

user = session.query(User).filter(User.id == '5').one()
print 'type:', type(user)
print 'id:', user.id
print 'name:', user.name
session.close()
