#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
asyncio可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。如果把asyncio用在服务器端，例如Web服务器，由于HTTP
连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。
asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。

'''
# 然后编写一个HTTP服务器，分别处理以下URL：
#     / - 首页返回b'<h1>Index</h1>'；
#     /hello/{name} - 根据URL参数返回文本hello, %s!。
import asyncio
from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    # return web.Response(body=b'<h1>index</h1>')
    return web.Response(text="Index")
async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    # app.router.add_route('GET', '/', index)
    app.add_routes([web.get('/', index)])
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app._make_handler(), '127.0.0.1', 9000)
    print('Server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
# 注意aiohttp的初始化函数init()也是一个coroutine，loop.create_server()则利用asyncio创建TCP服务。