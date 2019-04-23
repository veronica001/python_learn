#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
数据库表是一个二维表，包含多行多列。把一个表的内容用Python的数据结构表示出来的话，可以用一个list表示多行，
list的每一个元素是tuple，表示一行记录，

tuple表示一行很难看出表的结构。如果把一个tuple用class实例来表示，就可以更容易地看出表的结构来
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

[
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')
]
这就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。
但是由谁来做这个转换呢？所以ORM框架应运而生。
在Python中，最有名的ORM框架是SQLAlchemy。

SQLAlchemy用一个字符串表示连接信息：
'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'

ORM就是把数据库表的行与相应的对象建立关联，互相转换。
'''
from sqlalchemy import Column, String, create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    books = relationship('Book') # 一对多

class Book(Base):
    __tablename__ = 'Book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    user_id = Column(String(20), ForeignKey('user.id'))  # '多'的一方的book表通过外检关联到user表
# 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。

class School(Base):
    __tablename__ = 'school'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')

# Base.metadata.create_all(engine)  #创建表
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# DBSession对象可视为当前数据库连接。
# 创建session对象:
session = DBSession()
# 创建新User对象:
# new_user = User(id='5', name='Bob')
# 添加到session:
# session.add(new_user)
# new_book = Book(id='3', name='test3', user_id='5')
# session.add(new_book)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 有了ORM，查询出来的可以不再是tuple，而是User对象。SQLAlchemy提供的查询接口如下
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
print(user.books)
for book in user.books:
    print('book.id:%s book.name:%s  user_id:%s ' % (book.id, book.name, book.user_id))
# 关闭Session:
session.close()

'''
可见，ORM就是把数据库表的行与相应的对象建立关联，互相转换。
由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。

小结

ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。
正确使用ORM的前提是了解关系数据库的原理。
'''