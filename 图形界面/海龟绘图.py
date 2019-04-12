#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Python支持多种图形界面的第三方库，包括：
    Tk
    wxWidgets
    Qt
    GTK等等。

但是Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。
Tkinter
    我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；
    Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
    Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
    所以，我们的代码只需要调用Tkinter提供的接口就可以了。
'''
# 第一个gui
'''
在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，
所有的Widget组合起来就是一棵树。
pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
'''
# 第一步是导入Tkinter包的所有内容：
from tkinter import *
import tkinter.messagebox as messagebox

# 第二步是从Frame派生一个Application类，这是所有Widget的父容器
class Application(Frame):
    def __init__(self, master=None):
        # Frame.__init__(self, master)
        # super().__init__()
        super(Application,self).__init__() #tong shang deng jia
        self.pack()
        self.createWidgets()

    # 加入一个文本框，让用户可以输入文本，然后点按钮后，弹出消息对话框。
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text= 'hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'hello, %s' % name)
# 第三步，实例化Application，并启动消息循环：
app = Application()
app.master.title('hello')
# 主消息循环:
app.mainloop()