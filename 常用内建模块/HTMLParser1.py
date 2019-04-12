#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，看看里面的内容到底是新闻、
图片还是视频。

Python提供了HTMLParser来非常方便地解析HTML
特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。

handle_startendtag 处理开始标签和结束标签
handle_starttag 处理开始标签，比如<xx>
handle_endtag 处理结束标签，比如</xx>
handle_charref 处理特殊字符串，就是以&#开头的，一般是内码表示的字符
handle_entityref 处理一些特殊字符，以&开头的，比如
handle_data 处理数据，就是<xx>data</xx>中间的那些数据
handle_comment 处理注释
handle_decl 处理<!开头的，比如<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" handle_pi
处理形如<?instruction>的东西
'''
# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re



# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。

# 练习
# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，
# 输出Python官网发布的会议时间、名称和地点。
class MyHTMLParser(HTMLParser):
    def __init__(self):
        # super().__init__()   #这里super().__init__()和super(MyHTMLParser,self).__init__()是等价的
        super(MyHTMLParser, self).__init__()
        self.__parsedata = '' #设置一个标记，初始为空

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.__parsedata = 'name' # 通过属性判断如果该标签是我们要找的标签，设置标志位
        if tag == 'time':
            self.__parsedata = 'time'
        if ('class', 'event-location') in attrs:
            self.__parsedata = 'location'
        if ('class', 'say-no-more') in attrs:
            self.__parsedata = 'year'
    def handle_endtag(self, tag):
        self.__parsedata = '' # 在HTML 标签结束时，把标志位清空
    # def handle_startendtag(self, tag, attrs):
    #     print('<%s/>' % tag)

    def handle_data(self, data):
        if self.__parsedata == 'name':
            print('会议名称:', data)
        if self.__parsedata == 'year':
            if re.match(r'\s\d{4}', data):  # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
                print('year:',data)
        if self.__parsedata == 'location':
            print('location:',data)
            print('----------------------------------')
        if self.__parsedata == 'time':
            print('time:',data)
    # def handle_comment(self, data):
    #     print('<!--', data, '-->')

    # def handle_entityref(self, name):
    #     print('&%s;' % name)

    # def handle_charref(self, name):
    #     print('&#%s;' % name)

url = 'https://www.python.org/events/python-events/'
parser = MyHTMLParser()
with request.urlopen(url) as f:
    data = f.read()
    parser.feed(data.decode('utf-8'))