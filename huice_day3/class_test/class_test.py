# -*-coding:utf-8-*-

# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
# OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

# 面向过程 -- 程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。
# 面向对象 -- 程序设计把计算机程序视为一组对象的集合，用对象的调用来完成程序。

# 面向过程与面向对象的区别
# 以盖房子举例：
# 面向过程：我去买砖瓦水泥，我来砌墙，我去买门，我去做窗户，我去给房间布线，我来对房子进行装修；
# 面向对象：我让购买材料的人员去买砖瓦水泥，让泥瓦匠来砌墙，
# 让家具城的人给我送门窗过来，让电工来进行布线，找装修公司来进行装修。

# 区别在哪里？
# 第一种所有的事情都是你去做，
# 第二种所有的事情都有专门的人去做，我们负责指挥（调用）。
# 所谓面向对象编程思想，就是说要是有什么事情去做的话，不要上来就自己去干，
# 所有事情都自己干，如果事情很复杂，那么过程将会很乱，没有条理。而应该怎么样呢？
# 应该分工明确，分解这件事情，各司其职，当然这是要由我们去分解，由我们去创建对象，赋予他们职能。
# 具体的活，再让他们去干（调用）。

# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。
# 自定义的对象数据类型就是面向对象中的类（Class）的概念。
# python中面向对象有两个重要的主题，类和类的实例(对象)

# 类是对某一类具有共同特点的事物的抽象，是对象的定义，像是玩具的模具
# 类的实例（对象）是类的产物，它存放了类中定义的对象的具体信息，
# 像是生产线上根据同一个模具生产的不同规格的玩具

# 假设我们要处理学生的信息，为了表示一个学生的信息，面向过程的程序可以用一个dict表示：
dict1 = {'name': 'xiaoming', 'age': 20}
dict2 = {'name': 'xiaohong', 'age': 19}


def print_stuinfo(studict):
    print '%s: %s' % (studict('name'), studict('age'))


# 采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，
# 而是Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）。
# 如果要打印一个学生的信息，首先必须创建出这个学生对应的对象，
# 然后，调用对象的print_score方法，让对象自己把自己的数据打印出来。

# 类语法
# class 类名(继承的类的类名):
#     类体代码
# 注意：类名命名规则：名词，首字母大写，如果由多个单词组成，每个单词首字母都要大写
# 类包含成员变量和方法

class Student(object):
    "Student information"
    # 成员变量
    name = 'stu'
    age = 18

    # __init__()方法是一种特殊的方法。我们称之为初始化方法，
    # python在创建类的实例的时候，会调用这个类的__init__()方法
    # 类中的方法，参数中一定要传递self,self指的是对象自己
    # 我们根据图纸来建造房子，房子造好了，每个人都要回自己的家，self相当于门牌号
    def __init__(self, name, age):
        self.name = name  # 类中使用成员变量，用self.来访问
        self.age = age

    # 打印学生信息
    def print_stuinfo(self):
        print '%s: %s' % (self.name, self.age)


# 创建类的实例，并传递参数，这里传递的参数，由__init__()方法接收
student = Student('xiaoming', 20)
# 使用 实例.方法 来调用打印学生信息
student.print_stuinfo()
# 使用 实例.成员变量名 来访问成员变量(属性)
print student.name, student.age
# 用 类名.__doc__ 来查阅类的文档说明
print Student.__doc__

# __name__：类名
print Student.__name__
# __module__：模块名，如果类位于导入的一个模块中，返回模块的名称，
# 如果不是在导入模块中，返回__main__
print Student.__module__
# 类的所有父类组成的元组
print Student.__bases__
# 类的属性构成的字典
print Student.__dict__

# 对象销毁
del student
# print student

# 面向对象的三个特点：封装，继承，多态
# 封装：对数据的封装--》列表，元组，字典
#       对脚本语句的封装--》函数
#       对数据，方法的封装--》类
# 继承：子类继承父类的属性和方法
# 多态：不同对象对同一方法响应不同的情况
list1 = [3, 2, 6, 7, 8]

list1.append(9)
print list1

list1.sort()
print list1


# 定义一个子类，继承list，类体中，什么都不做
class SubList(list):
    pass


print '*' * 30
subList = [3, 2, 6, 7, 8]

subList.append(9)
print subList

subList.sort()
print subList


# 多态
# 如果子类中有属性或者方法与父类属性、方法名字一致，
# 会覆盖父类的属性和方法
class A(object):
    name = 'A'

    def fun(self):
        print 'A'


class B(A):
    pass
    # # 子类属性覆盖父类方法
    # name = 'B'
    #
    # # 子类方法覆盖父类方法
    # def fun(self):
    #     print 'B'


a = A()
a.fun()

b = B()
b.fun()
