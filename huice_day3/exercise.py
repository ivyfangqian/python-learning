# -*-coding:utf-8-*-

# 1、用户输入一个年份，判断这一年是不是闰年，如果是，打印 xxx年是闰年，如果不是，打印xxx年不是闰年
# 一:能被4整除，但不能被100整除的年份(例如2008是闰年，1900不是闰年)
# 或者
# 二:能被400整除的年份(例如2000年)也是闰年。
year = input('请输入年份：')

if type(year).__name__ != 'int':
    print '请输入正确年份'
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print '%d 是闰年' % year
    else:
        print '%d 不是闰年' % year

# 2、打印乘法表
# 1x1=1
# 1x2=2 	2x2=4
# 1x3=3 	2x3=6	3x3=9
# 1x4=4 	2x4=8 	3x4=12	4x4=16
# 1x5=5	    2x5=10	3x5=15	4x5=20	5x5=25
# 1x6=6	    2x6=12	3x6=18	4x6=24	5x6=30	6x6=36
# 1x7=7	    2x7=14	3x7=21	4x7=28	5x7=35	6x7=42	7x7=49
# 1x8=8	    2x8=16	3x8=24	4x8=32	5x8=40	6x8=48	7x8=56	8x8=64
# 1x9=9 	2x9=18 	3x9=27 	4x9=36 	5x9=45 	6x9=54 	7x9=63 	8x9=72 	9x9=81

for i in range(1, 10):  # 控制行数
    for j in range(1, i + 1):  # 控制每行打印的等式
        print str(j) + '*' + str(i) + '=' + str(j * i) + '\t',
    print '\n'

# 3、打印1-1000中的所有素数
# 素数，除了1和它本身以外不再有其他因数的数称为素数。
primeList = []
for num in range(1, 1001):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        primeList.append(num)

print primeList

# 4、求100－999中的水仙花数
# 若三位数abc，abc＝a^3+b^3+c^3， 则称abc为水仙花数。如153，1^3+5^3+3^3=1+125+27=153，则153是水仙花数
for number in range(100, 1000):
    a = number // 100
    b = (number - a * 100) // 10
    c = number - a * 100 - b * 10

    # 判断三个位数的3次幂的和是不是跟他它本身相等
    if a ** 3 + b ** 3 + c ** 3 == number:
        print number, 'is narcissus number.'


# 5、某公司的市内通话计费标准为:
# 三分钟内 0.2元
# 三分钟后每增加一分钟增加0.2元，不足一分钟按照一分钟算
# 要求编写程序，给定一个通话时间（单位：s），计算出收费金额


# 6、某市的出租车计费标准为：
# 3公里内10元，3公里以后每增加0.5公里加收1元，每等待2分钟加收1元
# 超过15公里加收原价50%的空驶费
# 每个写成一个函数
# 要求编写程序，对于任意给定的里程数（单位：km）和等待时间（单位：s）计算出应付车费

def taxi_cost(length, waitTime):
    # 费用
    cost = 10

    # 判断里程数输入是否合法
    if type(length).__name__ != 'int' and type(length).__name__ != 'float':
        print '里程数输入不合法'
        return

    # 判断等待时间输入是否合法
    if type(waitTime).__name__ != 'int' and type(waitTime).__name__ != 'float':
        print '等待时间输入不合法'
        return

    if length > 3:
        if (length - 3) % 0.5 == 0:
            cost = cost + (length - 3) / 0.5
        else:
            cost = cost + (length - 3) / 0.5 + 1
        if waitTime >= 120:
            if waitTime % 120 == 0:
                cost = cost + waitTime / 120
            else:
                cost = cost + waitTime / 120 + 1
    if length >= 15:
        cost = cost * 1.5
    return cost


print taxi_cost(12, 120)

