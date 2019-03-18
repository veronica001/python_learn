#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
collections是Python内建的一个集合模块，提供了许多有用的集合类。
    namedtuple:函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的
        某个元素。namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便
    namedtuple('名称', [属性list])
'''
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x, p.y)
# 要用坐标和半径表示一个圆，也可以用namedtuple定义
Circle = namedtuple('Circle', ['x','y','r'])

'''
deque:
    使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和
    删除效率很低。

    deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
    deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
'''
from collections import deque
q = deque(['x','y','z'])
q.append('a')
q.appendleft('b')
print(q)

'''
defaultdict:
    使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
    注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
    除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的

OrderedDict:
    使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict
    注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
'''
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'a'
print(dd['key1'])
print(dd['key2'])

from collections import OrderedDict

d = dict([('key1','a'), ('key2', 2), ('key3',3)])
print(d) #dict的key是无序的

od = OrderedDict([('key1',1), ('key2', 2), ('key3', 3)])
print(od) #od的key是有序的
od['z'] = 4
od['y'] = 5
od['x'] = 6
print(list(od.keys()))# 按照插入的Key的顺序返回

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, captain):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = captain

    def __setitem__(self, key, value):
        containKey = 1 if key in self else 0
        if len(self) - containKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containKey > 0:
            del self[key]
            print('del:', (key, value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self, key, value)

'''
ChainMap:
    ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，
    会按照顺序在内部的dict依次查找。
    
    什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还
    可以有默认参数。我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就
    使用默认参数。
'''
from collections import ChainMap
import os, argparse

# 构造缺省参数
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数
parse = argparse.ArgumentParser()
parse.add_argument('-u', '--user')
parse.add_argument('-c', '--color')
namespace = parse.parse_args()
command_line_args = {k:v for k, v in vars(namespace).items() if v}

# 组合成ChainMap
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
# 没有任何参数时，打印出默认参数：
# $ python3 use_chainmap.py
# color=red
# user=guest
#
# 当传入命令行参数时，优先使用命令行参数：
# $ python3 use_chainmap.py -u bob
# color=red
# user=bob
#
# 同时传入命令行参数和环境变量，命令行参数的优先级较高：
# $ user=admin color=green python3 use_chainmap.py -u bob
# color=green
# user=bob

'''
Counter:简单的计数器
'''
from collections import Counter
c = Counter()

for ch in 'programing':
    c[ch] = c[ch] + 1

print(c)
# Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次