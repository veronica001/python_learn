#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
由于在Python代码里拼字符串是不现实的，所以，模板技术出现了。
使用模板，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，而是嵌入了一些变量和指令，然后，
根据我们传入的数据，替换后，得到最终的HTML，发送给用户

MVC:
Python处理URL的函数就是C：Controller，Controller负责业务逻辑(mvc中的c)
包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。
MVC中的Model在哪？Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据

除了Jinja2，常见的模板还有：
    Mako：用<% ... %>和${xxx}的一个模板；
    Cheetah：也是用<% ... %>和${xxx}的一个模板；
    Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。

有了MVC，我们就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率。
'''


