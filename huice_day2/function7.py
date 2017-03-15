#-*-coding:utf-8-*-

# 函数就是将一些语句几种在一起的一个部件，
# 目的是减少我们同一段代码的复制粘贴，需要的时候以函数调用来代替，实现代码的复用
# 函数定义语法：
# def 函数名(0个或多个参数):
#     函数内要执行的代码
#     return 返回值

# 函数可以只定义函数名，没有参数，也没有返回值
def hello():
    print 'Hello World!'

# 函数的调用
res = hello()
print type(res)

# 函数有返回值
# 函数的命名规则：一个单词直接小写
# 多个单词，每个单词小写，以下划线分隔
def get_list():
    return [1,2,3,4]

aList  = get_list()
print type(aList),aList

# 函数可以有多个return语句，遇到return语句，跳出函数
def get_smaller(x,y):
    if x<y:
        return x
        print 'x is smaller'
    else:
        return y

smaller = get_smaller(1,2)
print smaller

# 函数有参数
# 参数：形参和实参,形参和实参要一一对应
def add(x,y):
    return x+y
sum = add(1,2)
print sum

# 参数传递不正确的情况
# sum = add()
# sum = add(1,2,3)

# 默认参数
# 为了提高程序的健壮性，
# 如果我们想在x，y值不传的时候，也给出一个默认的结果，就需要用到默认参数
# 参数有默认值之后，可以根据需要传递实参
def add(x =2,y=3):
    return x+y
sum = add()
print sum

sum = add(1)
print sum

sum = add(1,2)
print sum

# 函数的参数可以是任意类型
def print_item(x):
    print x
print_item(1)
print_item(1.0)
print_item('string')
print_item([1,2,3])
print_item((1,2,3))

# 函数的参数可以是不同类型
def print_userinfo(name,age):
    print 'username is %s and age is  %d'%(name,age)
print_userinfo('xiaoming',18)

# 可以将要传递的参数放在tuple中
aTuple = ('xiaoming',18)
print_userinfo(*aTuple)

def print_userinfo(name='name',age=18):
    print 'username is %s and age is  %d'%(name,age)

# 要传递的参数放在字典中
aDict = {'age':20,'name':'xiaoming'}
print_userinfo(**aDict)

# key不对应的情况
# aDict = {'height':20,'name':'xiaoming'}
# print_userinfo(**aDict)

# 可变长度的参数
def print_userinfo(name,age,*tuple_args,**dict_args):
    print 'username is %s and age is  %d'%(name,age)
    print tuple_args
    print dict_args

print_userinfo('xiaoming',18)

# 传递参数有冗余时，直接传递会报错，如何解决
# 冗余参数会传递到tuple_args
print_userinfo('xiaoming',18,170)

aTuple = ('xiaoming',18,170)
print_userinfo(*aTuple)

# 冗余参数存放到dict_args
print_userinfo(name = 'xiaoming',age = 18,height = 170)

# 重复传值给name参数
# print_userinfo('xiaoming',18, 170,name = 'xiaohong',height = 170)

# 冗余参数170，'xiaohong'存放到tuple_args,height = 170 存放到dict_args
print_userinfo('xiaoming',18, 170,'xiaohong',height = 170)


# 函数内部可以调用其他函数
def cal(x,y):
    print x+y
res =  cal(1,2)

# 如果一个函数在内部调用自身，这个函数叫做递归函数
# 举例：求一个数n的阶乘
# n的阶乘为n*(n-1)*(n-2)...*1
# n! = n*(n-1)！
# n为1的时候，阶乘为1
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n - 1)

print factorial(5)

# 变量的作用域问题
# 根据变量声明的位置的不同，变量存在不同的作用域：全局，局部
# 全局变量，局部变量
# 变量的作用域限制了你在哪个地方可以访问哪个变量
global_var = 'global'
def foo():
    local_var = 'local'
    print global_var+local_var

foo()

# foo中可以对所有的变量进行访问，但是函数外只能访问全局变量，无法访问函数的内部变量
# local_var是在函数体中定义的，只能在函数foo中使用
# global_var是在函数体外定义的，可以在脚本的任意一个位置访问
print global_var
# print local_var

# x = 'xiaoming'
# def fun():
#     x='xiaohong'
#     print x
# fun()
# print x

# 函数内部也可以定义全局变量
# 使用global关键字
# 注意：必须要先调用函数，函数体中定义的全局变量才能生效
# x = 'xiaoming'
# def fun():
#     x='xiaohong'
#     global global_y
#     global_y = 'xiaofang'
#     print x
# fun()
# print x
# print global_y

# 如何在函数中修改全局变量的值
x = 'xiaoming'
def fun():
    global x
    x='xiaohong'
    print x
fun()
print x

# 匿名函数,lambda
def func(x,y):
	return x+y
func = lambda x,y:x+y


# reduce()函数
list1 = [1,2,3]
def add(x,y):
    return x+y
print reduce(add,list1)
print reduce(lambda x,y:x+y,range(1,101))