#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
电子邮件收发过程
    Email从MUA（Mail User Agent——邮件用户代理。）发出去，不是直接到达对方电脑，而是发到MTA：Mail Transfer Agent——
    邮件传输代理，就是那些Email服务提供商，比如网易、新浪等等。由于我们自己的电子邮件是163.com，所以，Email
    首先被投递到网易提供的MTA，再由网易的MTA发到对方服务商，也就是新浪的MTA。这个过程中间可能还会经过别的MTA，
    Email到达新浪的MTA后，由于对方使用的是@sina.com的邮箱，因此，新浪的MTA会把Email投递到邮件的最终目的地
    MDA：Mail Delivery Agent——邮件投递代理。Email到达MDA后，就静静地躺在新浪的某个服务器上，存放在某个文件
    或特殊的数据库里，我们将这个长期保存邮件的地方称之为电子邮箱。
    同普通邮件类似，Email不会直接到达对方的电脑，因为对方电脑不一定开机，开机也不一定联网。对方要取到邮件，
    必须通过MUA从MDA上把邮件取到自己的电脑上。

    一封电子邮件的旅程就是：
    发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

要编写程序来发送和接收邮件，本质上就是：
    编写MUA把邮件发到MTA；
    编写MUA从MDA上收邮件。


发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，后面的MTA到另一个MTA也是用SMTP协议
收邮件时，MUA和MDA使用的协议有两种：POP：Post Office Protocol，目前版本是3，俗称POP3；IMAP：Internet
Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等。

Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

SMTP 端口25
login()方法用来登录SMTP服务器，
sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str

发送HTML邮件
    在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了

发送附件
    带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往
    里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可

发送图片
    要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用src="cid:0"就
    可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。

同时支持HTML和Plain格式
    办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件
    利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative

加密SMTP
    使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密
    SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
    只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接
'''
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
from email.header import Header
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return format((Header(name, 'utf-8').encode(), addr))

# from_addr = input('from:')
# pwd = input('password:')
# to_addr = input('to:')
# smtp_server = input('SMTP server:')

from_addr = '1474575568@qq.com'
pwd = 'rragrkjnibfbbabf'
to_addr = 'houshh@anchiva.com'
smtp_server = 'smtp.qq.com'

msg = MIMEMultipart('alternative')
# 第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，
# 最后一定要用utf-8编码保证多语言兼容性。
msg = MIMEText('hello, send msg by python,akjslfsalfjsdjf...', 'plain', 'utf-8')
# html
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

# 发送附件
# msg = MIMEMultipart()
# # 正文
# # msg.attach(MIMEText('hello, send with file...', 'plain', 'utf-8'))
# # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
# with open('../img/test.jpg', 'rb') as f:
#     # 设置附件的MIME和文件名，这里是png类型:
#     mime = MIMEBase('image', 'jpg', filename='test.jpg')
#     # 加上必要的头信息:
#     mime.add_header('Content-Disposition', 'attachment', filename='test.png')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # 把附件的内容读进来:
#     mime.set_payload(f.read())
#     # 用Base64编码:
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart:
#     msg.attach(mime)
#
# # 图片显示在正文中
# msg.attach(MIMEText('<html><head>hello</head><body><p>send with picture</p>' +
#                     '<img src="cid:0"/></body></html>', 'html', 'utf-8'))

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To']接收的是字符串而不是list
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应。
# server = smtplib.SMTP(smtp_server, 25)
server = smtplib.SMTP(smtp_server, 465)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, pwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

'''
小结：
构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，如果构造一个MIMEImage对象，就表示
一个作为附件的图片，要把多个对象组合起来，就用MIMEMultipart对象，而MIMEBase可以表示任何对象。它们的继承关系如下：
Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage

这种嵌套关系就可以构造出任意复杂的邮件。你可以通过https://docs.python.org/3/library/email.mime.html
文档查看它们所在的包以及详细的用法。
'''