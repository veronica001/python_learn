#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
了解了WSGI框架，我们发现：其实一个Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。
但是如何处理HTTP请求不是问题，问题是如何处理100个不同的URL。

WSGI提供的接口虽然比HTTP接口高级了不少，但和Web App的处理逻辑比，还是比较低级，我们需要在WSGI接口之上能进一步抽象，
让我们专注于用一个函数处理一个URL，至于URL到函数的映射，就交给Web框架来做。

由于用Python开发一个Web框架十分容易，所以Python有上百个开源的Web框架。这里我们先不讨论各种Web框架的优缺点，直接选择
一个比较流行的Web框架——Flask来使用。


除了Flask，常见的Python Web框架还有：
    Django：全能型Web框架；
    web.py：一个小巧的Web框架；
    Bottle：和Flask类似的Web框架；
    Tornado：Facebook的开源异步Web框架。

小结
    有了Web框架，我们在编写Web应用时，注意力就从WSGI处理函数转移到URL+对应的处理函数，这样，编写Web App就更加简单了。
    在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的。Web框架都提供了自己的API来实现这些功能。
Flask通过request.form['name']来获取表单的内容。
'''

# 处理3个URL，分别是：
#     GET /：首页，返回Home；
#     GET /signin：登录页，显示登录表单；
#     POST /signin：处理登录表单，显示登录结果。
#
# Flask通过Python的装饰器在内部自动地把URL和函数给关联起来
# Flask自带的Server在端口5000上监听

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'GET'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET', 'GET'])
def signin_form():
    return'''<form action='/signin' method='post'>
            <p>username<input name='username'></input></p>
            <p>password<input name='password' type='password'></input></p>
            <p><button type='submit'>Sign in</button></p>
        '''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>hello,admin</h3>'
    else:
        return '<h3>bad username or password</h3>'

if __name__ == '__main__':
    app.run()

'''
评论里的：
使用Python的Django框架开发的一个个人博客
http://www.tendcode.com/
博客功能：

    Django 自带的后台管理系统，方便对于文章、用户及其他动态内容的管理
    文章分类、标签、浏览量统计以及规范的 SEO 设置
    用户认证系统，在 Django 自带的用户系统的基础上扩展 Oauth 认证，支持微博、Github 等第三方认证
    文章评论系统，炫酷的输入框特效，支持 markdown 语法，二级评论结构和回复功能
    信息提醒功能，登录和退出提醒，收到评论和回复提醒，信息管理
    强大的全文搜索功能，只需要输入关键词就能展现全站与之关联的文章
    RSS 博客订阅功能及规范的 Sitemap 网站地图
    django-redis 支持的缓存系统，遵循缓存原则，加速网站打开速度
    实用的在线工具
    友情链接和推荐工具网站的展示

'''