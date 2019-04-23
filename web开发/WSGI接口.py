#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Web应用的本质就是：
    1.浏览器发送一个HTTP请求；
    2.服务器收到请求，生成一个HTML文档；
    3.服务器把HTML文档作为HTTP响应的Body发送给浏览器；
    4.浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和
响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。
这个接口就是WSGI：Web Server Gateway Interface。

WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。
有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML，通过start_response()发送Header，最后返回Body。

Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。所谓“参考实现”是指该实现完全
符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。

小结
    无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以
通过start_response()加上函数返回值作为Body。

    复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。
'''
# Header只能发送一次，也就是只能调用一次start_response()函数
# start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')]) #发送响应头
    return [b'<html><h1>hello, web!</h1></html>']

# application()函数就是符合WSGI标准的一个HTTP处理函数,它接收两个参数：
#     environ：一个包含所有HTTP请求信息的dict对象；
#     start_response：一个发送HTTP响应的函数。
# application()函数怎么调用？如果我们自己调用，两个参数environ和start_response我们没法提供，返回的bytes也没法发给浏览器。
# 所以application()函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器，我们可以挑选一个来用。
