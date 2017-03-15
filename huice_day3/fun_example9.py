#-*-coding:utf-8-*-

# 常用的python内置函数
# 数字相关函数
# 1、绝对值：abs(-1)
# 2、最大最小值：max([1,2,3])、min([1,2,3])，对序列进行操作
# 3、序列长度：len('abc')、len([1,2,3])、len((1,2,3))
# 4、取模：divmod(5,2)//(2,1)得到一个元组
# 5、乘方：pow(2,3,4)//2**3/4
# 6、浮点数：round(3.1415926,2)//3.14 四舍五入

print abs(-1)

list1 = [1,3,5]
print 'max is :%d'%max(list1)
print 'min is :%d'%min(list1)

print len(list1)

# help()查看函数帮助文档
help(divmod)
print divmod(5,2)

help(pow)
print pow(2,3) #2**3
print pow(2,3,4) #2**3%6

help(round)
print round(3.1415926,2)

# 功能相关函数
# 1、函数是否可调用：callable(funcname)，注意，funcname变量要定义过
# 2、类型判断：isinstance(x,list/int)
# 3、比较：cmp('hello','hello')
# 4、快速生成序列：(x)range([start,] stop[, step])

# callable(num)

num  = 1
print callable(num)

print callable(divmod)

# 类型判断
print isinstance(list1,list)
print isinstance(list1,tuple)

# cmp(x,y)比较x与y的内容是否相等，
# 相等返回0，x小于y 返回-1，x大于y 返回1
print 'x等于y ：%d'%cmp(1,1)
print 'x等于y ：%d'%cmp('aaa','aaa')
print 'x小于y ：%d'%cmp(1,2)
print 'x大于y ：%d'%cmp(2,1)
print cmp([1,2,3],[1,2,4])

# 生成序列，range(),xrange()
list2 =  range(1,11)
print type(list2),list2

# xrange()不生成list
print type(xrange(1,11)),xrange(1,11)
for i in xrange(1,11):
    print i

# 数据类型转换函数
# 1、int(x)
# 2、long(x)
# 3、float(x)
# 4、complex(x) //复数
# 5、str(x)
# 6、list(x)
# 7、tuple(x) //元组
# 8、hex(x)
# 9、oct(x)
# 10、chr(x)//返回x对应的字符，如chr(65)返回‘A'
# 11、ord(x)//返回字符对应的ASC码数字编号，如ord('A')返回65

str1 = '123'
print type(int(str1)),int(str1)
print type(long(str1)),long(str1)
print type(float(str1)),float(str1)
print type(complex(str1)),complex(str1)

int1 = 123
print type(str(int1)),str(int1)
print type(list(str1)),list(str1)
print type(tuple(str1)),tuple(str1)

# 数字不同进制的转换
print type(hex(int1)),hex(int1)
print type(oct(int1)),oct(int1)

# 返回ASCII码对应的字符
print chr(65)
print chr(97)

# 返回字符对应的ASCII码
print ord('A')
print ord('0')

# 字符串处理
# 1、首字母大写：str.capitalize()
# 2、字符串替换：str.replace()
# 3、字符串切割：str.split()
nameStr = 'xiaoming'

print nameStr.capitalize()

help(nameStr.replace)
print nameStr.replace('m','l')
print nameStr.replace('ming','hong')
print nameStr.replace('i','x')
print nameStr.replace('i','x',1)

help(nameStr.split)
ip = '192.168.2.1'
print ip.split('.')
print ip.split('.',2)

# 序列处理函数
# 1、len()序列长度
# 2、max()序列中最大值
# 3、min()最小值
# 4、filter()过滤序列
# 5、zip()并行遍历
# 6、map()并行遍历，可接受一个function类型的参数
# 7、reduce()递归

help(filter)

def is_even(x):
    if x%2==0:
        return True
print filter(is_even,range(1,11))

print filter(lambda x:x%2==0,range(1,11))

# zip(),并行遍历
name=['xiaoming','xiaohong','xiaofang','xiaogang']
age=[19,20,21,22]
city=['Beijing','Shanghai','Shenzhen','Hangzhou']
print zip(name,age,city)

# 如何序列的长度不同
name=['xiaoming','xiaohong','xiaofang','xiaogang']
age=[19,20,21]
city=['Beijing','Shanghai','Shenzhen','Hangzhou']
print zip(name,age,city)

# map：并行遍历，可接受一个function类型的参数
print map(None,name,age,city)

gender=['male','female']
print map(None,name,age,city)

a=[1,3,5]
b=[2,4,6]
print map(None,a,b)

print map(lambda x,y:x*y,a,b)

# reduce()归并
print reduce(lambda x, y: x + y, range(1,101))

# 练习
# 写一个函数，实现冒泡排序,按照升序排列

def bubble_sort(aList = []):
    if type(aList).__name__=='tuple':
        aList = list(aList)
    if type(aList).__name__=='list':
        if len(aList) <=1:
            return aList
        else:
            for i in range(0,len(aList)-1):
                for j in range(0,len(aList)-i-1):
                    if aList[j]>aList[j+1]:
                        aList[j], aList[j + 1] = aList[j + 1],aList[j]
    return aList

list1 = [20,10,50,30,90]
tuple1 = (20,10,50,30,90)
print bubble_sort(list1)
print bubble_sort(tuple1)


# 写一个函数，用递归的方法实现快速排序,按照升序排列
# 1. 快速排序就是选定一个标志位，我们把它叫做flag，
# 把小于flag的放在它的左边，把大于flag的放在它的右边，这样就以flag的分界，
# 把原来的list分为了两个子list ： list1 和 list2。
# 2. 按照上述方法，在list1 和 list2中再分别选flag，将list2 和 list2 分别拆成两个list，依次类推
# 3. 直到n = 1，即每个子list都只有一个元素  整个过程 : n/2x = 1  x = log2n

def quick_sort(aList = []):
    if len(aList)<=1:
        return aList
    else:
        flag = aList[0] #任意选一个值作为flag
        smallerList = [] #存放比flag小的值
        biggerList = [] #存放比flag大的值
        flags = []
        for i in aList:
            if i<flag:
                smallerList.append(i)
            elif i>flag:
                biggerList.append(i)
            else:
                flags.append(flag)

        # 递归调用
        smallerList = quick_sort(smallerList)
        biggerList = quick_sort(biggerList)

        return smallerList+flags+biggerList

list2sort = [30,20,10,90,80,50]
print quick_sort(list2sort)