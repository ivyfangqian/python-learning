#-*-coding:utf-8-*-

# 整数 num =1,可以是正数、负数、0
# 长整数 long = 111L，数字结尾以大写或小写的L标注，这里推荐大写L，小写容易与数字1混淆
# 浮点数 fl =1.2
# 复数 1+2j complex(1,2)
# 字符串 str= ‘string’
# 布尔值 True, False
# 列表 list = [1,2,3]
# 元组 tuple=(‘a’,’b’,’c’)
# 字典 dict = {name:’Harry’,age:12,height:150}
# 集合 s= set([1,1,2,2,3])
# 其中，数字（包含整数、长整数、浮点数、复数）、字符串、元组是不可变类型，列表、字典是可变类型
# 空值 None

# 整数
num=1
print type(num)

#查看我们变量的内存地址
print 'num:',id(num)
num1 = 1
print 'num1:',id(num1)
num = 2
print '重新复制后的num:',id(num)

# 长整型
long = 111L
print type(long)

# 浮点数
fl = 1.2
print type(fl)

# 复数
x = 1+2j
y = complex(3,4)
print type(x),type(y),x,y

# ------------------布尔值---------------------------------------------------------------------------
boo = True
boo_res = True and False
print boo
print boo_res
print boo and True
print 1>2 or 2<3

# ---------------字符串String,字符串是最常见的类型之一，可以用单引号或者双引号包裹-------------
str = 'Hello World!'
str = "Hello World!"
print type(str)

# 正确区分字符串与数字
str = '123'
print type(str)
int = 123
print type(int)

# 如何获取字符串中的值，可以直接通过索引来取值
# 或者通过切片操作来取值，[start:end],start<=x<end
print str[0]
print str[0:3]
print str[2:]
print str[:-1]

# 成员操作符 in/not in ，查看字符串中是否含有某个值
print 'e' in str
print 'll' in str

# 如何查看字符串长度
length = len(str)
print length

# 如何改变字符串
str = 'Hello'
print str

str = str + ' Python'
print str

# 字符串是不可变的
# str[0] = 'U'

# 字符串拼接,用加号+来拼接字符串,用*来进行重复操作
str = 'ab'+'cd'
print str,type(str)

str1='qwe'
print str1*2
print str1*3

# 转义字符\
me = 'I\'m Ivy.'
print me

me = 'I\'m Ivy.\\'
print me

# 如何清空与删除字符串
str = '' #空值
print str

del str #str为空，Null--》None
print str


# Python 支持格式化字符串的输出 。用法是将一个值插入到一个有字符串格式符%s 的字符串中。
print '我是 %s. 我今年 %d 岁.'%('Ivy',18)

# 常用内置的字符串处理函数
print dir(str)

# 列表--------------------------------------------------------------------------------------------------
# 列表List,Python内置的一种数据类型,
# list是一种有序的集合，可以随时添加和删除其中的元素,是可变类型
aList=[1,2,3]
print aList
print type(aList)
print len(aList)

# 切片取值,Python提供了切片（Slice）操作符，能大大简化这种操作,
# [0,3]==>[0,3),从索引为0开始取值，取到索引为3的值，但不包含3
print aList[0],aList[1],aList[2]
print aList[0:3]
print aList[1:3]
print aList[0:]
print aList[:3]
print aList[0:-1]

# 常见的list内置函数'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort','del'
print dir(aList)

persons = ['zhangsan','lisi','wangwu','zhaliu']
persons.append('zhangsan')
print persons
# index查询数组中某个元素的第一次出现的位置
print persons.index('zhangsan')
# 数组中是否含有某个元素
print persons.__contains__('zhangsan')
# insert往列表中插入数据
persons.insert(1,'haha')
print persons
# count计数
print persons.count('zhangsan')
# extend在列表末尾一次性追加另一个序列中的多个值
persons.extend(aList)
print persons
persons.extend(aList[0:2])
print persons
# del从列表中按照索引删除某个元素
del(persons[-1])
print persons
# remove删除第一个匹配的元素
persons.remove(1)
print persons
# pop弹出列表中的一个元素，默认是最后一个,并且返回这个元素的值
print persons.pop()
print persons
print persons.pop(-2)
print persons
# sort对列表进行排序,排序是按照ASCII码的顺序来排列，Z比a的顺序还要靠前
persons.sort()
print  persons
# reverse对列表中的元素进行反转
persons.reverse()
print persons

# 列表是可变类型
print id(persons)
persons[2] = 'zhaoliu'
print persons
print id(persons)

# 元组----------------------------------------------------------------------------
# 元组tuple也是python内置的一种数据类型，可以认为它是一种特殊的数组
# 元组是不可变类型，并且跟数组一样可以进行切片操作，以()来包裹
aTuple = ('ivy',20,'male',170)
print aTuple[0]
print aTuple[0:3]
print aTuple[:2]
print aTuple[0:]

# 试图改变tuple中的值，会报错
# aTuple[2]=21

# 字典----------------------------------------------------------------------------------
# 字典是python中唯一的映射类型，
# 字典是可变类型，
# 字典中的数据是无序的
# 一个字典条目的语法是 键:值，多条字典的条目被包裹在{}中
# 字母和数字可以作为条目的键
dict1 = {'name':'ivy','age':20,'gender':'male','height':170}
print dict1
# 从2.2版本开始，可以使用工厂方法dict()来创建字典
dict2 = dict((['x',1],['y',2]))
print  dict2
# 从2.3版本开始，可以使用内建方法fromkeys()方法来创建字典，
# 字典中的元素具有相同的值，如果没有给出默认值，则默认为None
dict3={}.fromkeys(('a','b'),1)
print dict3
dict4={}.fromkeys(('c','d'))
print dict4

# 可以直接使用dict1['key']来获取字典中某个键的值
print dict1['name']

# 判断字典中是否存在某个键
print 'name' in dict1
print 'aaa' in dict1
print 'aaa' not in dict1

# 打印字典中所有的键
print dict1.keys()

# 打印字典中所有的值
print dict1.values()

dict1['age']=21
print dict1

# 取字典中的键值对
print dict1.items()

# 访问字典中的值，只需要遍历字典中的键
for key in dict1.keys():
    print 'key=%s,value=%s'%(key,dict1[key])

for key in dict1:
    print 'key=%s,value=%s'%(key,dict1[key])

# 删除字典中的条目，或者清空字典中的内容
del dict1['height']
print dict1

print dict1.pop('age')
print dict1

dict1.clear()
print dict1

del dict1
# print dict1

# 查看字典的元素数量
print len(dict2)

# 集合类型 Set-----------------------------------------------------------------------------------
# 数学中，把set称做由不同的元素组成的集合，set的成员通常我们叫做集合元素
# python把这个概念引入到集合类型对象里，集合对象是一组无序排列的元素的集合
# 集合是无序的，所以不能为集合创建索引或执行切片，集合没有键值对应，也不能通过键来获取元素中的值
# 集合由两种类型，可变集合set和不可变集合frozenset

s = set('peppa')
print s

g = frozenset('george')
print g

print len(g)

print s==g

# 如何访问set中的值
print 'p' in s
print 'p' in g
for i in s:
    print i

# 如何对集合进行操作，注意，只能对可变集合进行修改，不可变集合修改会报错
s.add('z')
print s

s.update('dog')
print s

s.remove('z')
print s

# 不可变集合强行修改会报错哦
# g.add('z')

print s.pop()
print s


s1=set([1,2,3,4,6,5,4,3])
print s1

# None -- Python中的Null对象
# python中一个特殊的类型，被称为Null对象或者NoneType，它不支持任何运算，也没有任何的方法
aNone = None
print aNone

# 数据类型转换----------------------------------------------------------------------------------
# 不同数据类型之间的转换
# 字典可以转换为字符串，列表，元组类型
dic =  {'name':'ivy','age':20}
print type(str(dic)),str(dic)

print type(list(dic)),list(dic)

print type(tuple(dic)),tuple(dic)

#元组可以转换为字符串，也可以转换为列表，但不可以转换为字典
tu = (1,2,3)
tu2str = tu.__str__()
print type(tu2str),tu2str

tu2list = list(tu)
print type(tu2list),tu2list

#列表可以转换为字符串，也可以转换为元组，但也不可以转换为字典
li = ['w','o','r','l','d']
li2str = li.__str__()
print type(li2str),li2str

li2tuple = tuple(li)
print type(li2tuple),li2tuple

print ''.join(li)
print '-'.join(li)

# 字符串转换为列表、元组、字典
s = 'world'

str2list = list(s)
print type(str2list),str2list

str2tuple = tuple(s)
print type(str2tuple),str2tuple

s1 = "{'name':'ivy','age':20}"
str2dict = eval(s1)
print type(str2dict),str2dict