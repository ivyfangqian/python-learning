# -*-coding:utf-8-*-

# get请求
import urllib,urllib2,json

url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=13801380000"

request = urllib2.Request(url)
print request

response_data = urllib2.urlopen(request)
response = response_data.read().decode('gbk').encode('utf-8')

print response


# post请求
post_url = "http://www.gellefreres.com/gfLogin/login"
post_data = {}
post_data['username'] = '18701336131'
post_data['password'] = '96e79218965eb72c92a549dd5a330112'

post_data_urlencode = urllib.urlencode(post_data)
post_req  = urllib2.Request(post_url,post_data_urlencode)
print post_req

post_res_data = urllib2.urlopen(post_req)
post_res = post_res_data.read()
print post_res

res_dict = json.loads(post_res)

errorCode = res_dict['errorCode']
isSuccess = res_dict['success']
try:
    assert (errorCode==0 and isSuccess),'登录失败！'
except AssertionError as loginError:
    print loginError




# 查看快递信息接口
print '查看快递信息接口开始测试'

url = "http://www.kuaidi100.com/query?type=yuantong&postid=200423509764"

request = urllib2.Request(url)

response_data = urllib2.urlopen(request)
response = response_data.read()

dict_kd = json.loads(response)
print dict_kd
print dict_kd['data']
