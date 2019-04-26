#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
在一个Web App中，所有数据，包括用户信息、发布的日志、评论等，都存储在数据库中。在awesome-python3-webapp中，我们选择MySQL作为数据库。

Web App里面有很多地方都要访问数据库。访问数据库需要创建数据库连接、游标对象，然后执行SQL语句，最后处理异常，清理资源。这
些访问数据库的代码如果分散到各个函数中，势必无法维护，也不利于代码复用。

所以，我们要首先把常用的SELECT、INSERT、UPDATE和DELETE操作用函数封装起来。

由于Web框架使用了基于asyncio的aiohttp，这是基于协程的异步模型。在协程中，不能调用普通的同步IO操作，因为所有用户都是由一
个线程服务的，协程的执行速度必须非常快，才能处理大量用户的请求。而耗时的IO操作不能在协程中以同步的方式调用，否则，等待一
个IO操作时，系统无法响应任何其他用户。

这就是异步编程的一个原则：一旦决定使用异步，则系统每一层都必须是异步，“开弓没有回头箭”。

幸运的是aiomysql为MySQL数据库提供了异步IO的驱动。
'''
import asyncio, aiomysql
import logging


# 创建连接池
# 使用连接池的好处是不必频繁地打开和关闭数据库连接，而是能复用就尽量复用。
@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = aiomysql.create_pool(
        host = kw.get('host' , 'localhost'),
        port = kw.get('port', 3306),
        user = kw['user'],
        password = kw['password'],
        charset = kw.get('charset', 'utf8'),
        autocommit = kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

# 要执行SELECT语句，我们用select函数执行，需要传入SQL语句和SQL参数
async def select(sql, args, size=None):
    logging(sql, args)
    global __pool
    with (await  __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        # SQL语句的占位符是?，而MySQL的占位符是%s，select()函数在内部自动替换。注意要始终坚持使用带参数的SQL，
        # 而不是自己拼接SQL字符串，这样可以防止SQL注入攻击。
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = cur.fetchmany(size)
        else:
            rs = cur.fetchall()
        await cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs

# 要执行INSERT、UPDATE、DELETE语句，可以定义一个通用的execute()函数，因为这3种SQL的执行都需要相同的参数，以及返回一个整
# 数表示影响的行数
# execute()函数和select()函数所不同的是，cursor对象不返回结果集，而是通过rowcount返回结果数。
async def execute(sql, args, size=None):
    logging(sql, args)
    global __pool
    with (await __pool) as conn:
        try:
            cur = conn.cursor()
            await cur.execute(sql.replace('?', '%s') % args or ())
            affects = cur.rowcount()
            await cur.close
        except BaseException as e:
            raise
        return affects

def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)

# 定义所有ORM映射的基类Model
# Model从dict继承，所以具备所有dict的功能，同时又实现了特殊方法__getattr__()和__setattr__()，因此又可以像引用普通字段那样写
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'"Model" object has no attribute "%s"' % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default vale for %s: %s' % (key, str(value)))
                setattr(self, key, value)
        return value
# 有了基本的select()和execute()函数，我们就可以开始编写一个简单的ORM了。
# 设计ORM需要从上层调用者角度来设计。