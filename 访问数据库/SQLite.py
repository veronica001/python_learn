#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，
经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。
Python就内置了SQLite3,直接使用。
在使用SQLite前，我们先要搞清楚几个概念：
    表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，等等。表和表之间通过外键关联。
    要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
    连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。

使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。
使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。

如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))

小结

在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。
如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？请回忆try:...except:...finally:...的用法。
'''

# 练习
# 请编写函数，在Sqlite中根据分数段查找指定的名字：
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
# 连接到SQLite数据库
# 数据库文件是test.db,如果文件不存在，会自动创建:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    # ' 返回指定分数区间的名字，按分数从低到高排序 '
    # 我的思路：先查询符合指定区间的分数，然后对分数进行排序。然后再循环查询数据库根据分数取出名字
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select score from user where score >? and score <= ? ', (low, high))
    scorelist = cursor.fetchall()

    length = len(scorelist)
    while i < (length - 1):
        if scorelist[i] > scorelist[i+1]:
            tmp = scorelist[i]
            scorelist[i] = scorelist[i+1]
            scorelist[i+1] = tmp
        i += 1
        if length == 1:
            break
        if i == (length - 1):
            i = 0
            length -= 1
    namelist = []
    for i in range(len(scorelist)):
        cursor.execute('select name from user where score=?', (scorelist[i][0],))
        name = cursor.fetchall()
        namelist.append(name[0][0])
    cursor.close()
    conn.commit()
    conn.close()
    return namelist


# 优秀作业，结合以前学习的map,还有查询数据库可以直接排序：
def get_score_in(low, high):
    try:
        con = sqlite3.connect(db_file)
        cursor = con.cursor()
        cursor.execute(r"select * from user where score > ? and score <= ? order by score", (low, high))
        values = list(map(lambda t: t[1], cursor.fetchall()))
        print(values)
        return values
    finally:
        print('2')
        cursor.close()
        con.close()

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')

'''
有return的情况下try catch finally的执行顺序
结论：
1、不管有没有出现异常，finally块中代码都会执行；
2、当try和catch中有return时，finally仍然会执行；
3、finally是在return后面的表达式运算后执行的（此时并没有返回运算后的值，而是先把要返回的值保存起来，
    不管finally中的代码怎么样，返回的值都不会改变，任然是之前保存的值），所以函数返回值是在finally执行前确定的；
4、finally中最好不要包含return，否则程序会提前退出，返回值不是try或catch中保存的返回值。
'''