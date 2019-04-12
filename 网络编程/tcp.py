#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的
IP地址和端口号，再指定协议类型即可。
大多数连接都是可靠的TCP连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。

AF_INET：指定使用IPv4协议
AF_INET6：IPv6
SOCK_STREAM: 指定使用面向流的TCP协议
80 端口是Web服务的标准端口
SMTP服务是25 端口，FTP服务是21 端口
端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。
recv(max):接收数据，一次最多接收指定的字节数

TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。
'''
import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com', 80)) #参数是一个tuple，包含地址和端口号。
# 建立TCP连接后，我们就可以向新浪服务器发送请求，要求返回首页的内容
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    b = s.recv(1024)
    if b:
        buffer.append(b)
    else:
        break
data = b''.join(buffer)

# 接收完数据后，调用close()方法关闭Socket，这样，一次完整的网络通信就结束了
s.close()

header,html = data.split(b'\r\n', 1)
# print(header.decode('utf-8'))
# 将网页内容保存到文件里
with open('sina.html', 'wb') as f:
    f.write(html)

'''
服务器：
        服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，
    随后的通信就靠这个Socket连接了。
    一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。
    服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，
    
    服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，也可以用0.0.0.0绑定到所有的网络地址，还可以用127.0.0.1绑定到
    本机地址。127.0.0.1是一个特殊的IP地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，也就是
    说，外部的计算机无法连接进来。
'''
# 我们来编写一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去。

# 创建socket
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定地址和端口号
s1.bind(('127.0.0.1',9999))
# 监听,传入的参数指定等待连接的最大数量
s1.listen(5)
print('waiting for connection...')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % (addr))
    sock.send(b'welcome!')
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 循环接收处理连接
while True:
    sock, addr = s1.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


