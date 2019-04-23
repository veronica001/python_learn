#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
在Web应用中，服务器把网页传给浏览器，实际上就是把网页的HTML代码发送给浏览器，让浏览器显示出来。而浏览器和服务器之间的
传输协议是HTTP
    HTML是一种用来定义网页的文本，会HTML，就可以编写网页；
    HTTP是在网络上传输HTML的协议，用于浏览器和服务器的通信。

GET表示一个读取请求，将从服务器获得网页数据，/表示URL的路径，URL总是以/开头，/就表示首页，最后的HTTP/1.1指示采用的HTTP协
议版本是1.1。目前HTTP协议的版本就是1.1，但是大部分服务器也支持1.0版本，主要区别在于1.1版本允许多个HTTP请求复用一个TCP连
接，以加快传输速度。
Content-Type指示响应的内容，这里是text/html表示HTML网页。请注意，浏览器就是依靠Content-Type来判断响应的内容是网页还是图
片，是视频还是音乐。

HTTP请求
    步骤1：浏览器首先向服务器发送HTTP请求，请求包括:get,post等
    步骤2：服务器向浏览器返回HTTP响应，响应包括：
        响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；
        响应类型：由Content-Type指定
        以及其他相关的Header
    步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。
    HTTP协议同时具备极强的扩展性，虽然浏览器请求的是http://www.sina.com.cn/的首页，但是新浪在HTML中可以链入其他服务器的
    资源，比如<img src="http://i1.sinaimg.cn/home/2013/1008/U8455P30DT20131008135420.png">，从而将请求压力分散到各个服务
    器上，并且，一个站点可以链接到其他站点，无数个站点互相链接起来，就形成了World Wide Web，简称“三达不溜”（WWW）。

HTTP格式
    每个HTTP请求和响应都遵循相同的格式，一个HTTP包含Header和Body两部分，其中Body是可选的。
        GET /path HTTP/1.1
        Header1: Value1
        Header2: Value2
        Header3: Value3
        每个Header一行一个，换行符是\r\n。

        POST /path HTTP/1.1
        Header1: Value1
        Header2: Value2
        Header3: Value3

        body data goes here...

        当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。

        HTTP响应的格式：
        200 OK
        Header1: Value1
        Header2: Value2
        Header3: Value3

        body data goes here...

当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip，所以，看到Content-Encoding: gzip时，需要将Body数据
先解压缩，才能得到真正的数据。压缩的目的在于减少Body的大小，加快网络传输。
'''