#! /usr/bin/env python
# -*- coding: utf-8 -*

'''
Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。

定义常量时，用大写变量通过整数来定义(类型必须是int,实际上还是变量)
更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能

value属性则是自动赋给成员的int常量，默认从1开始计数
如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
'''
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
    print(name ,'=>', member, member.value)

from enum import Enum, unique

'''
@unique装饰器可以帮助我们检查保证没有重复值。
'''
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# 访问这些枚举类型可以有若干种方法
day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
Weekday.Mon
print(day1 == Weekday(1))
# Weekday(7)报错
'''
可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
'''
# 练习：把Student的gender属性改造为枚举类型，可以避免使用字符串：
@unique
class Gender(Enum):
    Male = 0
    Female = 1

# Gender = Enum('Gender',('Male', 'Female'))
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')