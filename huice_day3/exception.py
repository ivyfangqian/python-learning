# -*-coding:utf8-*-

# Exception
# python标准异常：
# http://blog.csdn.net/wmj2004/article/details/53215939

# ImportError:导入模块错误
# import A

# IndexError:索引超出范围
# list1 = [1,2,3]
# print list1[3]

# KeyError:字典中不存在的键
# dict1 = {'name':'ivy','age':20,'gender':'female'}
# print dict1['height']

# NameError：访问没有定义的变量
# print a

# IndentationError:缩进错误
# if 1==1:
# print 'aaa'

# SyntaxError:语法错误
# list2 = [1,2,3,4

# TypeError:不同类型间的无效操作
# print 1+'1'

# ZeroDivisionError:除数为0
# print 5/0

# 如何检测并处理这些异常：try
# 两种方法
# 第一种：
# try:
#   检测代码
# except Exception [as reason]:
#   出现异常后的处理代码

# try:
#     sum = 1+'1'
# except TypeError:
#     print '救命啊，TypeError，类型错误'

# 获取出错原因
# try:
#     sum = 1+'1'
# except TypeError as reason:
#     print '救命啊，TypeError，类型错误 \n %s'%reason


# 可能有多个异常
# 注意：当try中的语句出现错误后，代码就不会再往下继续执行了
# try:
#     res = 5 / 0
#     sum = 1+'1'
# except TypeError as reason:
#     print '救命啊，TypeError，类型错误 \n %s'%reason
# except ZeroDivisionError as reason:
#     print '救命啊，ZeroDivisionError，除数为零错误 \n %s'%reason


# 可以捕获所有异常，但是不推荐
# try:
#     res = 5 / 0
#     sum = 1+'1'
# except :
#     print '救命啊，出错了'

# 第二种
# # try:
#   检测代码
# except Exception [as reason]:
#   出现异常后的处理代码
# finally:
#   无论如何都会被执行的代码
# try:
#     res = 5 / 0
#     sum = 1+'1'
# except TypeError as reason:
#     print '救命啊，TypeError，类型错误 \n %s'%reason
# except ZeroDivisionError as reason:
#     print '救命啊，ZeroDivisionError，除数为零错误 \n %s'%reason
# finally:
#     print '无论如何，我都会出现'

# raise语句
# raise

# raise ZeroDivisionError('除数为零错误')
