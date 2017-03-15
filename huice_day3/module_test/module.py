# -*-coding:utf-8-*-

# 封装
# 容器--》对数据的封装（列表、元组、字典）
# 函数--》对语句的封装
# 类--》对属性和方法的封装
# 模块--》模块就是程序，任何一个.py文件就是一个模块

import hello

# 命名空间
# hi()
hello.hi()

# 导入模块
# 1、import 模块名
# 2、from 模块名 import 函数名（a,b,c/*）
# 3、import 模块名 as 新名称

# 考虑命名空间
import CurrencyConverter

print '100美元可以兑换 %.2f 人民币'%CurrencyConverter.dollar2rmb(100)
print '100元人民币可以兑换 %.2f 美元'%CurrencyConverter.rmb2dollar(100)

#
# from CurrencyConverter import dollar2rmb,rmb2dollar
from CurrencyConverter import *  #不推荐，可能会导致同名函数被覆盖

print '100美元可以兑换 %.2f 人民币'%dollar2rmb(100)
print '100元人民币可以兑换 %.2f 美元'%rmb2dollar(100)

import CurrencyConverter as cc

print '100美元可以兑换 %.2f 人民币'%cc.dollar2rmb(100)
print '100元人民币可以兑换 %.2f 美元'%cc.rmb2dollar(100)