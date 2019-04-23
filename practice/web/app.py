#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
处理3个URL，分别是：
    GET /：首页，返回登录页面；
    GET /signin：登录页，显示登录表单；
    POST /signin：处理登录表单，显示登录结果。
    GET /signup : 注册用户

'''
from flask import request,Flask,render_template
from sqlalchemy import Column, String, create_engine,ForeignKey,Integer
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(5), primary_key=True, autoincrement=True)
    name = Column(String(20))
    pwd = Column(String(20))
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer(5), primary_key=True)
    name = Column(String(20))
    user_id = Column(Integer(5), ForeignKey='user.id')

# 初始化数据库连接:
engine = create_engine('mysql+mysql-connector://root:123456@127.0.0.1:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# Flask类的实例为wsgi应用程序，第一个参数是应用模块或者包的名称
app = Flask(__name__)

#  route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数
@app.route('/', ['GET'])
def home():
    return render_template('form.html')

@app.route('/signup', ['GET'])
def signup():
    return render_template('signup.html')

@app.route('/add', ['Post'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    session = DBSession()
    new_user = User(name = username, pwd = password)
    session.add(new_user)
    return render_template('form.html', message='注册成功', username = username)