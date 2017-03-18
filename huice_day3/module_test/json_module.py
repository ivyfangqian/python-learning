# -*-coding:utf-8-*-

# 字典
stu1 = {'name': 'xiaoming', 'age': 20, 'height': 170}
print stu1

stu2 = {'name': '小红', 'age': 20, 'height': 165}
print stu2

# 定义字典时如果包含了中文，打印字典时中文会以16进制显示，不会直接显示中文。
# 可以用json模块来解决这个问题
import json

print json.dumps(stu2, ensure_ascii=False)

# JSON(JavaScript Object Notation, JS 对象标记) 是一种轻量级的数据交换格式。
# 对象表示为键值对
# 数据由逗号分隔
# 花括号保存对象
# 方括号保存数组
# JSON最常用的格式是对象的 键值对。例如下面这样：
# {"firstName": "Brett", "lastName": "McLaughlin"}

# 手机号信息查询接口
# https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=13801380000

# json模块使用时，需要import json
# json.dumps(),编码，字典转换为字符串
json_stu1 = json.dumps(stu1)
print type(json_stu1), json_stu1

# json.loads(),字符串转为编码
# json.loads()，解码，json字符串转换为字典
dict_stu1 = json.loads(json_stu1)
print type(dict_stu1), dict_stu1

# 以上面我们获取手机号信息为例
mobile_json = "{'mts':'1380138',\
'province':'北京',\
'catName':'中国移动',\
'telString':'13801380000',\
'areaVid':'29400',\
'ispVid':'3236139',\
'carrier':'北京移动'}"

# 标准的json格式是key和value都以双引号来包裹
mobile_json = mobile_json.replace("'",'"')

print mobile_json
print type(mobile_json)

mobile_dict = json.loads(mobile_json,encoding="utf-8")
print mobile_dict.keys()
print mobile_dict.values()
print mobile_dict['province']

# unicode转为utf-8
# for i in mobile_dict.values():
#     print i.encode('utf-8')

