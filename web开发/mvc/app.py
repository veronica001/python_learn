#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
把上次直接输出字符串作为HTML的例子用高端大气上档次的MVC模式改写一下
Flask通过render_template()函数来实现模板的渲染。和Web框架类似，Python的模板也有很多种。Flask默认支持的模板是jinja2

通过MVC，我们在Python代码中处理M：Model和C：Controller，而V：View是通过模板处理的，这样，我们就成功地把Python代码和
HTML代码最大限度地分离了。

在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。
很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令
'''

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['Get', 'Post'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['Get'])
def sign_form():
    return render_template('form.html')

@app.route('/signin', methods=['Post'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('sign_ok.html' ,username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()

