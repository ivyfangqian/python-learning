# -*-coding:utf-8-*-

# 1、定义一个函数，函数参数为长方形的高和宽，
# 函数根据传入的参数打印一个长方形,用户传入长方形的高：height，宽：width，则打印长方形
# 例如：
# height:4 width:6
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *

def print_rectangle(height=0, width=0):
    # 如果长或者宽是0，直接返回
    if height == 0 or width == 0:
        return

    for i in range(0, height):  # 控制行数
        for j in range(0, width):  # 控制*打印
            print '*',
        print ''


print_rectangle(4, 6)


# 2、餐馆：创建一个名为Restaurant的类，
# 其方法__init__()设置两个属性：restaurant_name和cuisine_type。
# 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，
# 其中前者打印前述两项信息，而后者打印一条信息，指出餐馆正在营业。
class Restaurant(object):
    restaurant_name = 'haogaoxing'
    cuisine_type = 'noodle'

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print self.restaurant_name
        print self.cuisine_type

    def open_restaurant(self):
        print self.restaurant_name, '餐馆正在营业'


sta = Restaurant('bugaoxing', 'xican')
sta.describe_restaurant()
sta.open_restaurant()

# 3、写一个程序，用于计算2008年10月1日是这一年的第几天？（2008年1月1日是这一年的第一天）
import time

date_str = '2008-10-1'
date_tuple = time.strptime(date_str, '%Y-%m-%d')
print date_tuple[-2]


# 4、传入两个日期，2017-01-17,2017-03-17,打印两个日期之间所有的日期
def print_date(start_time, end_time):
    # 将开始时间、结束时间转为tuple格式
    start_tuple = time.strptime(start_time, '%Y-%m-%d')
    end_tuple = time.strptime(end_time, '%Y-%m-%d')

    # 将tuple格式的时间转为时间戳
    start_sec = time.mktime(start_tuple)
    end_sec = time.mktime(end_tuple)

    # 定义一个list盛放符合条件的日期
    date_list = []
    date_sec = start_sec + 24 * 60 * 60
    while date_sec < end_sec:
        # 将时间转为可读格式再进行存储
        tmp = time.strftime('%Y-%m-%d', time.localtime(date_sec))
        date_list.append(tmp)

        # 时间加一天
        date_sec += 24 * 60 * 60
    print date_list


print_date('2017-3-1', '2017-3-10')


# 5、定义类：Animal
# 包含属性 name，color，legs,私有属性__gender
# 包含方法 set_name，set_color,set_legs,set_gender
# 可以设置animal的名字，颜色，腿的数量
# get_name，get_color,get_legs,get_gender
# 返回，animal的名字，颜色，腿的数量
#
# 定义类:Runable
# 包含方法：run
#
# 定义类：Flyable
# 包含方法：fly
#
# 定义类：Dog，继承Animal、Runable类
# 重写类Runable的run方法
# 并创建实例进行调用
#
# 定义类：Bird，继承Animal、Flyable类
# 重写类Flyable的fly方法
# 并创建实例进行调用

class Animal(object):
    name = 'animal'
    color = 'white'
    legs = 4
    __gender = 'male'

    def set_name(self, name):
        self.name = name

    def set_color(self, color):
        self.color = color

    def set_legs(self, legs):
        self.legs = legs

    def set_gender(self, gender):
        self.__gender = gender

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_legs(self):
        return self.legs

    def get_gender(self):
        return self.__gender

class Runnable(object):
    def run(self):
        print 'run run run ~~~'

class Flyable(object):
    def fly(self):
        print 'fly fly fly ~~~'

class Dog(Animal,Runnable):
    def run(self):
        print 'A dog is running.'

class Bird(Animal,Flyable):
    def fly(self):
        print 'A bird is flying.'