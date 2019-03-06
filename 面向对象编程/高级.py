#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
__slots__:  限制class的实例任意添加属性
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
'''

class Student(object):
    __slots__ = ('name', 'age')   # 用tuple定义允许绑定的属性名称


'''
在绑定属性时，虽然写起来简单，但是暴露了属性，并且无法检查合法性。此时可以在类里添加set_xxx()来设置属性并检查合法性，
同时添加get_xxx()来获取该属性。
但上述操作略复杂。
Python内置的@property装饰器就是负责把一个方法变成属性调用的

把一个getter方法变成属性，只需要加上@property就可以了，
此时，@property本身又创建了另一个装饰器@score.setter，
负责把一个setter方法变成属性赋值

只定义getter方法，不定义setter方法就是一个只读属性

@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
'''


class Student1():
    __width = 0
    __height = 0

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integex!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self.__score = value

    # age就是只读属性
    @property
    def age(self):
        return self.__birth


a = Student1()
a.score = 80
print(a.score)
a.score = 99
print(a.score)


# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('wrong width type')
        if value < 0:
            raise ValueError('width value must be >0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError('wrong height type!')
        if value < 0:
            raise ValueError('width value must be >0')
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

'''
多重继承：
    通过多重继承，一个子类可以同时获得多个父类的所有功能
    
'''
class Animal(object):
    pass
# 哺乳类
class Mammal(Animal):
    pass
class Birds(Animal):
    pass
class Runable(Animal):
    pass
class Flyable(Animal):
    pass

class Dog(Mammal, Runable):
    pass

'''
在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，
通过多重继承就可以实现，比如，让Ostrich(鸵鸟)除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层
次的复杂的继承关系。
只允许单一继承的语言（如Java）不能使用MixIn的设计。
'''
# 为了更好地看出继承关系，可以把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。

# Python自带的很多库也使用了MixIn eg
# class myTcpserver(TCPServer, ForkingMixIn):
#     pass
#
# class MyUDPServer(UDPServer, ThreadingMixIn):
#     pass


'''
定制类
__str__
__repr__
__iter__: 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象,
    ，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
__getitem__： Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取具体某个元素
        要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
__setitem__, __delitem__
__getattr__:动态返回一个属性，可以针对完全动态的情况作调用。
'''
class A(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'A object name: %s' % self.name
    __repr__ = __str__
    # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，
    # 这样，我们就有机会返回score的值：
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda:25  #返回函数也行，使用a.age()调用
# print(A('test'))
# 打印 <__main__.A object at 0x00000000023AD7F0>，不好看，定义好__str__()方法，返回一个好看的字符串就可以了：
a = A('test')
a #在命令行打印仍然是显示地址，这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看
# 到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：__repr__ = __str__

# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
class Fib(object):
    __list = [0, 1]
    def __init__(self):
        self.a, self.b = 0,1

    # def __iter__(self):
    #     sum = self.a + self.b
    #     self.__list.append(sum)
    #     self.a = self.b
    #     self.b = sum
    #     return self.__list
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值 a, b = b, a+b  (先计算，后赋值)
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    def __getitem__(self,n):
        a ,b = 1,1
        # 添加切片操作
        if isinstance(n, int):
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            L = []
            if start is None:
                start = 0
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

f = Fib()
print(f[6])
print(f[:7])
print(f[2:5])
print(f[-1:-2])