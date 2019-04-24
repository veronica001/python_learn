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
from practice.web.db  import DBSession,User

# Flask类的实例为wsgi应用程序，第一个参数是应用模块或者包的名称
app = Flask(__name__)

#  route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数
@app.route('/', methods=['GET'])
def home():
    return render_template('form.html')

@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/add', methods=['Post'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    session = DBSession()
    new_user = User(name=username, pwd=password)
    session.add(new_user)
    session.commit()
    session.close()
    return render_template('form.html', message='注册成功', username = username)

@app.route('/signin', methods=['Post'])
def signin():
    username = request.form['username']
    password = request.form['password']
    session = DBSession()
    user = session.query(User).filter(User.name==username).first()
    if user == None:
        return render_template('form.html', message='用户名不存在', username=username)
    if user.name == username and user.pwd == password:
        return render_template('sign_ok.html', username=username)
    else:
        return render_template('form.html', message='用户名或密码不正确', username=username)

if __name__ == '__main__':
    app.run()
