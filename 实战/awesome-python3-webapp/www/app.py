#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Web App建立在asyncio的基础上，因此用aiohttp写一个基本的app.py：
# logging.basicConfig()函数是一个一次性的简单配置工具，也就是说只有在第一次调用该函数时会起作用，后续再次调用该函数时
# 完全不会产生任何操作的，多次调用的设置并不是累加操作。
import logging
logging.basicConfig(level=logging.INFO)

import asyncio
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type' : 'text/html'})

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app._make_handler(), '127.0.0.1', 8000)
    print('Server start on http://127.0.0.1:8000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()