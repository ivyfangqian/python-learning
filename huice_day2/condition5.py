#-*-coding:utf-8-*-

# python流程控制，python代码的执行顺序分为：顺序、分支、循环
# 顺序执行很简单，就是从第一行一条一条执行，直到最后一行执行结束
print '第一行脚本'
print '第二行脚本'

# 分支，也叫条件语句，在不同的条件下，执行不同的代码块
# 常用的分支语句：if，if  else ,if elif，if elif else
# 第一种：if
# if 条件表达式:
#   条件表达式为真时，执行此代码块

age = 15
if age<=28 and age>=14:
    print '团员'
else:
    print '年龄不合法'


# 第二种：if else
# if 条件表达式:
#   条件表达式为真时，执行此代码块
# else:
#   条件表达式为假时，执行此代码块
age = 9
if age<=28 and age>=14:
    print '团员'
else:
    print '年龄不合法'

# 密码password为123456，用户输入密码如果与此密码一致，则提示密码输入正确，否则提示密码输入错误
password = '123456'
pass_input = raw_input('请输入密码：')
if pass_input==password :
    print '密码输入正确'
else:
    print '密码输入错误'

# elif即else-if语句
# python中没有switch语句，所以多个条件时，可以用elif来实现
# 第三种：if elif
# if 条件表达式A:
#   条件表达式为真时，执行此代码块
# elif 条件表达式B:
#   条件表达式B为真时，执行此代码块
# 举例：成绩小于60的输出不及格，大于等于60小于80的输出及格，
# 大于等于80小于90的输出良好，大于等于90小于等于100的，输出优秀
# 其他输入，输出 输入成绩不合法提示
score = -1
if score>=0 and score<60:
    print '成绩不及格'
elif  score>=60 and score < 80:
    print '及格'
elif  score>=80 and score < 90:
    print '良好'
elif  score>=90 and score <= 100:
    print '优秀'

# 第四种：if elif else
# if 条件表达式A:
#   条件表达式为真时，执行此代码块
# elif 条件表达式B:
#   条件表达式B为真时，执行此代码块
# else:
#   以上表达式都为假时，执行此代码块
# 举例：成绩小于60的输出不及格，大于等于60小于80的输出及格，
# 大于等于80小于90的输出良好，大于等于90小于等于100的，输出优秀
# 其他输入，输出 输入成绩不合法提示
score = 95
if score>=0 and score<60:
    print '成绩不及格'
elif  score>=60 and score < 80:
    print '及格'
elif  score>=80 and score < 90:
    print '良好'
elif  score>=90 and score <= 100:
    print '优秀'
else:
    print '输入成绩不合法'

# if-else语句的嵌套
if score>=0 and score<=100:
    if score < 60:
        print '成绩不及格'
    elif score >= 60 and score < 80:
        print '及格'
    elif score >= 80 and score < 90:
        print '良好'
    elif score >= 90:
        print '优秀'
else:
    print '输入成绩不合法'

# 三元表达式，X if C else Y，C是条件表达式，X是条件表达式为真的结果，Y是条件表达式为假时的结果
# 举例：比较x，y的值，并输出其中的最小值
x = 4
y = 3

if x<y:
    smaller = x
else:
    smaller = y

# 有了三元表达式，可以写成
smaller = x if x<y else y
print smaller

# 练习题
# 1、用户输入一个数字，判断这个数字是否能够被3整除，如果能够被整除，则输出，xx是3的倍数，否则输出xx不是3的倍数
# 2、根据传入的月份来输出，这个月有几天(默认2月有28天，不考虑闰年)

month = 5
days = 0
if month in [1,3,5,7,8,10,12]:
    print '%d 月有 31天'%(month)
elif month in [4,6,9,11]:
    print '%d 月有 30天' % (month)
elif month==2:
    print '%d 月有 28天' % (month)
else:
    print '输入不合法'


