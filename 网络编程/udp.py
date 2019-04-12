#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。

SOCK_DGRAM: 指定了这个Socket的类型是UDP
recvfrom()方法返回数据和客户端的地址与端口

UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，
.也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。
'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(('127.0.0.1', 9999))
# s.bind(('',9999))
s.bind(('localhost'), 9999)
print('bind udp on 9999...')
while True:
    data, addr = s.recvfrom(1024)
    print('recv from %s:%s' % addr)
    s.sendto(b'hello %s!' % data, addr)