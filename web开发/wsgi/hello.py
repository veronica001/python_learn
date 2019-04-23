#! /usr/bin/env python
# -*- coding: utf-8 -*-
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')]) #发送响应头
    body = '<h1>hello, %s</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]