#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Filename:db.py

from sqlalchemy import Column, String, create_engine,ForeignKey,Integer
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    pwd = Column(String(20))
    # books = relationship('Book')

# class Book(Base):
#     __tablename__ = 'book'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(20))
#     user_id = Column(Integer, ForeignKey='user.id')

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)