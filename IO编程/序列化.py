#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
在程序运行的过程中，所有的变量都是在内存中
一旦程序结束，变量所占用的内存就被操作系统全部回收,如果没有把修改后的xxx值存储到磁盘上，下次重新运行程序，变量又被
初始化为初始值。

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，
marshalling，flattening等等，都是一个意思。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
pickle模块来实现序列化。

pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
pickle.dump()直接把对象序列化后写入一个file-like Object：
'''
import pickle
d = dict(name='bob', age=13)
print(pickle.dumps(d))

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
'''
当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。

这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。

Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，
只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
'''
f1 = open('dump.txt', 'rb')
d = pickle.load(f1)
f1.close()
print(d)


'''
Json:
    如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON
    表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更
    快，而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
    JSON类型 	Python类型
    {} 	        dict
    [] 	        list
    "string" 	str
    1234.56 	int或float
    true/false 	True/False
    null 	    None    
    
Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
dumps()方法返回一个str，内容就是标准的JSON。
dump()方法可以直接把JSON写入一个file-like Object

要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取
字符串并反序列化
JSON标准规定JSON编码是UTF-8
'''
# 把python对象变成json
import json
print(json.dumps(d))
json_str = '{"name": "bob", "age": 13, "score":85}'
print(json.loads(json_str))

'''
JSON进阶：

'''