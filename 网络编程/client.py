#! /usr/bin/env python
# -*- coding: utf-8 -*-
import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #udp
# s.connect(('127.0.0.1', 9999)) udp不需要这一步

# print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    # s.send(data)
    s.sendto(data, ('127.0.0.1', 9999)) #udp发送方法
    print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
s.close()