# -*-coding:utf8-*-

import urllib

url = "http://www.baidu.com"

# urllib.open(url)可以根据url获取到一个连接
res = urllib.urlopen(url)

# 连接成功后，可以使用read(),readline(),readlines(),close()方法对内容进行操作
# print res.read()

# info(),getcode(),geturl()
print res.info()
print res.getcode()
print res.geturl()

res.close()


url1 = "http://www.baidu.com?kw=qwer!@#"

# 使用urllib.quote函数对url进行url编码，编码的符号不包含/
print urllib.quote(url1)

# 使用urllib.qupte函数对url进行url编码，编码的符号包含/
print urllib.quote_plus(url1)

# 可用urllib.unquote()对url进行url解码
print urllib.unquote('http%3A//www.baidu.com%3Fkw%3Dqwer%21%40%23')

# 可用urllib.unquote()对url进行url解码
print urllib.unquote_plus('http%3A%2F%2Fwww.baidu.com%3Fkw%3Dqwer%21%40%23')


params = urllib.urlencode({'username':'xiaoming','password':'123456'})
print params

# urllib发送get请求
kd_get_res = urllib.urlopen('http://www.kuaidi100.com/query?type=yuantong&postid=200423509764')
print kd_get_res.read()

# urllib发送post请求
kd_post_res = urllib.urlopen('http://www.kuaidi100.com/query','type=yuantong&postid=200423509764')
print kd_post_res.read()

# urllib与urllib2需要配合使用：
# urllib2可以接受Request类来设置url请求的headers，urllib仅可以接受url；


# urllib提供urlencode方法生成请求参数字符串，
# urllib2没有；
# urllib2仅有quote无quote_plus相关方法；

import urllib2

# urllib2发送get请求
url = "http://www.kuaidi100.com/query?type=yuantong&postid=200423509764"
url_req = urllib2.Request(url)
url_res_data = urllib2.urlopen(url_req)
print url_res_data.read()

# urllib2发送post请求
url = "http://www.kuaidi100.com/query"
post_data = 'type=yuantong&postid=200423509764'
url_req = urllib2.Request(url,post_data)
url_res_data = urllib2.urlopen(url_req)
print url_res_data.read()


# urlparse对url进行拆分，拆分为6个元素，存储到一个元组中
import urlparse
test_url = 'http://www.kuaidi100.com/query?type=yuantong&postid=200423509764'
parse_url = urlparse.urlparse(test_url)
print parse_url