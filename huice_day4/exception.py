# -*-coding:utf8-*-

# 在程序运行过程中，总会遇到各种各样的错误。
# 有的错误是程序编写有问题造成的，比如本来应该输出整数结果输出了字符串，这种错误我们通常称之为bug，bug是必须修复的。
# 有的错误是用户输入造成的，比如让用户输入email地址，结果得到一个空字符串，这种错误可以通过检查用户输入来做相应的处理。
# 还有一类错误是完全无法在程序运行过程中预测的，比如写入文件的时候，磁盘满了，写不进去了，或者从网络抓取数据，网络突然断掉了。
# 这类错误也称为异常，在程序中通常是必须处理的，否则，程序会因为各种问题终止并退出。
# Python内置了一套异常处理机制，来帮助我们进行错误处理。

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

# IO错误
# file = open('aaa.txt')

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


# else语句,当没有出错的时候执行else中的语句
# try:
#     print '没有错误的时候执行else'
#     # 5/0
# except:
#     print '出错了'
# else:
#     print '我是else，没有exception的时候执行我'

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

# 例如我们最后一定要关闭文件
# try:
#     file = open('d:\\test\\test01.txt')
#     file.write('aaaaaaaaaa')
# except IOError as ioerror:
#     print ioerror
# finally:
#     file.close()

# 如果有函数调用，什么时候捕获异常好呢
# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
# 比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
# 也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。
# 这样一来，就大大减少了写try...except...finally的麻烦。
# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('0')
#     except ZeroDivisionError, e:
#         print 'ZeroDivisionError!'
#     finally:
#         print 'finally...'
#
#
# main()


# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。

# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     bar('0')
#
#
# main()

# 出现错误，我们一般情况下，希望程序给我们把日志记录下来，好帮助我们判断是哪里出了错误
# Python内置的logging模块可以非常容易地记录错误信息：
# 像如下例子，同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
import logging


# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('0')
#     except ZeroDivisionError, e:
#         logging.exception(e)
#
#
# main()
# print '我们的程序继续执行了'

# 抛出错误
# Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
# raise语句
# raise语句如果不带参数，就会把当前错误原样抛出
# raise

# class FooError(StandardError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
# foo(0)


# 只有在必要的时候才定义我们自己的错误类型。
# 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），
# 尽量使用Python内置的错误类型。

# 最后我们来看一种最常见的错误处理方式
# def foo(s):
#     n = int(s)
#     return 10 / n
#
# def bar(s):
#     try:
#         return foo(s) * 2
#     except ZeroDivisionError, e:
#         print 'Error!'
#         raise ValueError('invalid value: %s' % s)
#
# def main():
#     bar('0')
#
# main()


