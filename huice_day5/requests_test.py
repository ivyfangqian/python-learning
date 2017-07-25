# -*-coding:utf8-*-

import requests

class HttpRequestTest(object):
    def send_get_req(self,url,data):
        res = requests.get(url,params=data)
        res_dict = res.json()
        return res_dict

    def send_post_req(self,url,data):
        res = requests.post(url,data)
        res_dict = res.json()
        return res_dict

# import unittest
# url = "http://www.kuaidi100.com/query"
# data = {"type":"yuantong","postid":"200423509764"}
#
# req = HttpRequestTest()
# res = req.send_get_req(url,data)
# print res["status"]
# assert res["status"]=="200"




