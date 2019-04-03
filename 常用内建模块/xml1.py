#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
DOM vs SAX
    操作XML有两种方法：DOM和SAX。
        DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
        SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
    正常情况下，优先考虑SAX，因为DOM实在太占内存。
    在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，
    然后就可以解析xml了。

解析XML时，注意找出自己感兴趣的节点，响应事件时，把节点数据保存起来。解析完毕后，就可以处理数据。
关于XMLParser Objects的方法介绍下
    详见python文档：xml.parsers.expat
    xmlparser.StartElementHandler(name, attributes) #遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典
    xmlparser.EndElementHandler(name)   遇到XML结束标签时调用。
    xmlparser.CharacterDataHandler(data)
    #调用时机：
    #从行开始，遇到标签之前，存在字符，content 的值为这些字符串。
    #从一个标签，遇到下一个标签之前， 存在字符，content 的值为这些字符串。
    #从一个标签，遇到行结束符之前，存在字符，content 的值为这些字符串。
    #标签可以是开始标签，也可以是结束标签。
'''
from xml.parsers.expat import ParserCreate

#利用SAX解析XML文档牵涉到两个部分: 解析器和事件处理器
#解析器负责读取XML文档，并向事件处理器发送事件，如元素开始跟元素结束事件。
#而事件处理器则负责对事件作出响应，对传递的XML数据进行处理


class DefaultSaxHandler(object):
    def start_element(self, name, attr):
        print('sax:start_element, name:%s attr %s' % (name, str(attr)))
        #name表示节点名称，attrs表示节点属性（字典）
    def end_element(self,name):
        print('sax: end_element, name:%s' % name)
    def char_data(self, text):
        # text表示节点数据
        print('sax:char_data: %s' % text)

#为了方便理解，我已经在下面还原来解析过程，
#标出何时调用，分别用S：表示开始；E：表示结束；D：表示data
# xml = r'''<?xml version="1.0"?>
# S<ol>C
# C    S<li><a href="/python">Python</a></li>EC
# C    S<li><a href="/ruby">Ruby</a></li>EC
# S</ol>E
# '''

xml = r'''<?xml version="1.0"?>
<ol>
    S<li><a href="/python">Python</a></li>
    S<li><a href="/ruby">Ruby</a></li>
</ol>
'''
# 处理器实例
handler = DefaultSaxHandler()
# 解析器实例
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
#开始解析XML
parser.Parse(xml)
#然后就是等待expat解析，
#一旦expat解析器遇到xml的 元素开始，元素结束，元素值 事件时
#会回分别调用start_element, end_element, char_data函数

# 如果要生成复杂的XML呢？建议你不要用XML，改成JSON。

# 练习
# 请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
# https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woe
# id%20%3D%202151330&format=xml
# 参数woeid是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。



from urllib import request
def parseXml(xml_str):
    print(xml_str)
    return {
        'city': '?',
        'forecast': [
            {
                'date': '2017-11-17',
                'high': 43,
                'low' : 26
            },
            {
                'date': '2017-11-18',
                'high': 41,
                'low' : 20
            },
            {
                'date': '2017-11-19',
                'high': 43,
                'low' : 19
            }
        ]
    }

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
