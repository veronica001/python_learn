#! /usr/bin/env python
# -*- coding: utf-8 -*

'''
类和实例
在Python中，定义类是通过class关键字：
class Student(object):
    pass
类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的通常，
如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去

和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别

小结：
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，
虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
'''

# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了,，必须传入与__init__方法匹配的参数，但self不需要传
# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def print_scroe(self):
#         print('%s %s ' % (self.name, self.score))
# bart = Student()
# 可以自由地给一个实例变量绑定属性
# bart.name = "test"
# print(bart.name)
# print(Student)

# test = Student("jay", 85)
# test.print_scroe()


'''
访问限制：
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的.约定俗成认为是私有变量

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器
对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量（避免这么操作）

总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。
'''

# 这样实例变量.__name就无法从外部访问内部变量
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_scroe(self):
        print('%s %s ' % (self.__name, self.__score))
    # 外部代码需要获取内部变量，可通过添加方法获取
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    # 修改变量， 在方法中设置，可以对参数做检查，避免传入无效的参数
    def set_score(self, score):
        if 0 < score < 100:
            self.__score = score
        else:
            return ValueError("bad score")


class Student1(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        # if gender == 'female' or gender == 'male':
        if gender in ['female', 'male']:
            self.__gender = gender
        else:
            return ValueError("bad value")

# 测试:
bart = Student1('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


'''
继承和多态：
在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
而被继承的class称为基类、父类或超类（Base class、Super class）。

继承有什么好处？最大的好处是1.子类获得了父类的全部功能。2.需要我们对代码做一点改进

当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。

所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。
Dog可以看成Animal，但Animal不可以看成Dog。

多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，
因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思

开闭原则：
    对扩展开放：允许新增Animal子类；
    对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
    
静态语言 vs 动态语言
    对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
    对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
    这就是动态语言的“鸭子类型”,，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
    
    Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
    但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，
    你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

小结
继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
'''

class Animal(object):
    def run(self):
        print('animal is running...')

class Dog(Animal):
    def run(self):
        print('dog is running...')
    def eat(self):
        print('eating meat... ')

class Cat(Animal):
    def run(self):
        print('cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

dog = Dog()
cat = Cat()
dog.run()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(dog)
run_twice(Tortoise())

class Timer(object):
    def run(self):
        print('Start...')

run_twice(Timer())


'''
获取对象信息
    type():获取对象类型
        判断一个对象是否是函数类型使用types.FunctionType    eg:  type(fn)==types.FunctionType
    isinstance():对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
        能用type()判断的基本类型也可以用isinstance()判断
     总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。 
    dir(): 获得一个对象的所有属性和方法,它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
        >>> dir('ABC')
        ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
    类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()
    函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
'''

'''
实例属性和类属性：
    直接在class中定义属性，这种属性是类属性。这个属性虽然归类所有，但类的所有实例都可以访问到
    
    在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
    但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
    
小结
    实例属性属于各个实例所有，互不干扰；
    类属性属于类所有，所有实例共享一个属性；
    不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
'''

class Student2(object):
    # 类属性
    name = '类属性'

s = Student2()
print(s.name)

# 练习：统计学生人数，每增加一个实例，该属性自动增加

class Student3():
    count = 0
    def __init__(self, name):
        self.__name = name
        Student3.count += 1

# 测试:
if Student3.count != 0:
    print('测试失败!')
else:
    bart = Student3('Bart')
    if Student3.count != 1:
        print('测试失败!')
    else:
        lisa = Student3('Bart')
        if Student3.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student3.count)
            print('测试通过!')
