# -*-coding:utf-8-*-

# python中我们会经常用到time模块
# 使用import time来引入time模块

import time

# 常见的time模块函数

# 时间戳是以秒为单位的浮点数，
# 以1970年1月1日午夜到现在所经过的时间来表示

print time.time()

# 返回时间元组,time.localtime([seconds])
# tm_wday=5, 一个周的第几天，0代表周一
# tm_yday=77，一年的第几天
print time.localtime()

# 返回执行时间戳的时间元组
now = time.time()
print time.localtime(now-100000)
print time.localtime(0)

# time.mktime(tuple_time)，返回时间戳
# 默认截断小数位
tuple_time = time.localtime()
print time.mktime(tuple_time)

# time.asctime([tuple_time])
# 根据时间元组，返回Sat Mar 18 17:03:21 2017格式的时间
# 参数不传，默认返回当前时间
print time.asctime()

print time.asctime(time.localtime())

# time.ctime([seconds])
# 根据时间戳，返回Sat Mar 18 17:04:01 2017格式的时间
# 参数不传，默认返回当前时间
print time.ctime(now)

print time.ctime(time.time())

# time.strftime(format[,tuple_time])
# 根据传入的格式化字符串，将tuple时间格式化为指定的格式
#  python中时间日期格式化符号：
# %y     两位数的年份表示（00-99）
# %Y     四位数的年份表示（000-9999）
# %m    月份（01-12）
# %d     月内中的一天（0-31）
# %H    24小时制小时数（0-23）
# %I      12小时制小时数（01-12） 
# %M    分钟数（00=59）
# %S      秒（00-59）
# tuple_time可以不传，不传返回当前时间格式化后的结果
print time.strftime('%Y-%m-%d %H:%M:%S')

print time.strftime('%H:%M:%S %m/%d/%Y')

print time.strftime('%Y-%m-%d')

# 获取一个小时前的时间
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()-3600))

# time.strptime(string, format)
# 传入的时间为字符串
# 按照传入的format解析字符串时间为tuple格式的时间
print time.strptime('2017-03-15 08:00:00','%Y-%m-%d %H:%M:%S')

print time.strptime('17:27:33 03/18/2017','%H:%M:%S %m/%d/%Y')


# time.sleep(seconds)
# 等待,延时
time.sleep(1)
print '等待1秒'

time.sleep(2)
print '等待2秒'



