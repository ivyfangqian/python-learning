#-*-coding:utf-8-*-

#我们的第一个程序
print 'Hello World!'

# 打印中文需要设置coding为utf-8
print '房倩，你好!'

# 'print 可以同时打印多个字符串，两个字符串之间以都好隔开
print '房倩，','你好!'


# python单行注释为#，
# 多行注释也推荐使用#
# print 'Hello World!'
# print 'Hello World!'
# print 'Hello World!'

# Python允许用'''...'''，"""..."""的格式表示多行内容
print '''单引号，第一行
单引号，第二行'''

print """双引号，第一行
双引号，第二行"""

#输出数字
print 1

#输出运算结果
print 1+2

# 输出组合结果,需要注意的是，这里1+2=是字符串
print '1+2=',1+2

# 等待用户输入raw_input(),input(),其中input()输入内容必须是一个合法的Python表达式
# name = raw_input("请输入你的名字：")
# print name,'你好！'
#
# name = input("请输入你的名字：")
# print name,'你好！'
#
# result = input("请输入1+2的结果：")
# print result

# 为了让程序员有一个良好的代码习惯，python强制要求用缩进来标识一个函数或者类的范围
# 输出一个数字的绝对值
a = 1
if a >= 0:
    print a
else:
    print -a