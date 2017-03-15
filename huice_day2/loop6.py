#-*-coding:utf-8-*-

# 当我们需要重复执行某一代码块的时候，会用到循环操作
# 循环语句包含 while ，for
# while 条件表达式:
#   条件表达式为真时执行代码
# 例如：输出1-10
i=0
while i<=10:
    print i
    i+=1

# range(start,end,step),step为空默认为1
#从0到10(不包含10)
print range(10)
#从1到10(不包含10)
print range(1,10)
#从1到10，间隔2(不包含10)
print range(1,10,2)

# 举例：求1-10的所有数字的和
num = 0
sum = 0
while num <= 10:
    sum = sum + num
    num += 1
print 'sum =' + sum.__str__()

#无限循环/死循环
# i=0
# while True:
#     print i
#     i+=1

# python提供给我们另一个最强大的循环机制就是for循环语句，它可以遍历序列成员（字符串、数组、元组）
# 迭代序列有三种方法
# 第一种：通过序列项迭代，类似于Java中的for each
# 语法：for  iter_var in iterable:
#              要循环执行的代码块
# 例如：我们要遍历一个字符串中的所有字符
aStr =  'rabbit'
for eachLetter in aStr:
    print eachLetter

# 遍历列表中的每一个元素
nameList = ['xiaoming','xiaohong','xiaofang','xiaogang']
for eachName in nameList:
    print eachName

# 第二种，通过序列的索引来遍历序列
# 通过序列的索引,nameIndex从0开始，0=<nameIndex<3
for nameIndex in range(len(nameList)):
    print nameIndex,nameList[nameIndex]

# 第三种，同时使用项和索引迭代
for j,eachName in enumerate(nameList):
    print j,eachName

# 举例：求1-10的所有数字的和
sum = 0
for num in range(1,11):
    sum = sum + num
print 'sum is %d'%(sum)

# 练习:分别使用while与for循环输出1-100之间的所有偶数

# python循环中使用else语句
# 其他语言中，只在分支语句中才能见到else，
# python则不然，循环语句中使用else，代表在循环正常结束后，执行else中的代码块，
# break语句也会跳过else
sum = 0
for num in range(1,11):
    sum = sum + num
else:
    print 'sum is %d'%(sum)

# 强制结束循环，遇到break结束循环的情况时，不执行else
# import time
# for num in range(30):
#     print num
#     time.sleep(1)
# else:
#     print 'bye'


while True:
    print i
    if i>=100:
        break
    i+=1
else:
    print 'break跳出循环'



# python中使用pass，pass是占位语句，什么都不做，只是为了保证程序结构的完整性
for num in range(1, 11):
    print num
    if num>=8:
        pass
    print '='*20



# break与continue
# break，结束循环
# ocntinue，跳出本次循环

for x in range(10):
    if x>5:
        break
    print x

for x in range(10):
    if x<5:
        continue
    print x

# 循环嵌套，Python 语言允许在一个循环体里面嵌入另一个循环体。
#举例：对列表[50,20,30,10]进行冒泡排序,按照升序排列
# 冒泡排序：从前往后将相邻的两个数进行比较，将较小的数放在前面，较大的数放在后面
# 第一轮
# 20 50 30 10
# 20 30 50 10
# 20 30 10 50
# 第二轮
# 20 30 10 50
# 20 10 30 50
# 第三轮
# 10 20 30 50
# 冒泡排序原理: 每一轮只能将一个数归位, 如果有n个数进行排序,只需将n-1个数归位,
# 也就是说要进行n-1轮操作(已经归位的数不用再比较)
aList = [20,30,10,50]

for i in range(len(aList)-1): #比较几轮,第一轮：0，第二轮：1，第三轮：2
    for j in range(0,len(aList)-i-1): #定义比较的索引,第一轮，0-1,1-2,2-3，第二轮：0-1,1-2，第三轮：0-1
        if aList[j] > aList[j+1]:
            aList[j],aList[j + 1] = aList[j+1],aList[j]
        print aList


