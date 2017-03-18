# -*-coding:utf-8-*-

# 包（package）
# 一个python的工程可能包含成百上千的python文件，
# 我们如果将所有文件都放在一个目录下，将是一件非常恐怖的事情
#包是一个有层次的文件目录结构
# 它定义了一个由模块和子包组成的python应用程序执行环境

# 1、为平坦的名称空间加入有层次的组织结构
# 2、允许程序员把有联系的模块组合到一起
# 3、允许分发者使用目录结构而不是一大堆混乱的文件
# 4、帮助解决有冲突的模块名称

# 怎么去创建一个包呢
# 包中需要创建一个__init__.py文件,文件内容可以为空
# __init__.py成为初始化模块

# 如何使用包中的模块，两种方法
# 第一种：import 包.子包.模块
# 第一种：import 包.子包.模块
# 第二种：from 包.子包 import 模块

import test.CurrencyConverter as cc
print '100rmd = %.2f dollar'%cc.rmb2dollar(1000)

from test import CurrencyConverter
print '100dollar = %.2f rmb'%CurrencyConverter.dollar2rmb(1000)

# 含有子包的时候
import test.conversion.LengthConversion
print '100cm = %.2f inch'%test.conversion.LengthConversion.in2cm(100)

import test.conversion.LengthConversion as lc
print '100cm = %.2f inch'%lc.cm2in(100)

from test.conversion import LengthConversion
print '10inch = %.2f cm'%LengthConversion.in2cm(10)

# python是自带电池的
# Wiki百科的解释：
# Motto of the Python programming language, meaning it comes with a large library of useful modules.
# Python编程语言的格言，意味着Python拥有大量含有有用模块的库。
# 优雅、明确，简单
# 电池：python的标准库
# python标准库中包含一般任务所需要的模块
# python不只带着电池，还可以充电
import timeit
# 模块的文档
print timeit.__doc__

# 查看所有的可以被外部调用的方法
print timeit.__all__

# 模块存放的路径
print timeit.__file__




