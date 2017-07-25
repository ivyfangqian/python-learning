# -*-coding:utf8-*-

import unittest
from huice_day5.requests_test import HttpRequestTest


class KuaidiInfoTest(unittest.TestCase):
    url = "http://www.kuaidi100.com/query"
    def setUp(self):
        self.http_test = HttpRequestTest()

    def tearDown(self):
        pass

    def test_type_null(self):
        data = {"type": "", "postid": "200423509764"}
        res_data = self.http_test.send_get_req(self.url,data)
        self.assertEquals(res_data["status"],"400")
    def test_postid_null(self):
        data = {"type": "yuantong", "postid": ""}
        res_data = self.http_test.send_get_req(self.url, data)
        self.assertEquals(res_data["status"], "400")
    def test_type_error(self):
        data = {"type": "shentong", "postid": "200423509764"}
        res_data = self.http_test.send_get_req(self.url, data)
        self.assertEquals(res_data["status"], "201")
    def test_postid_error(self):
        data = {"type": "yuantong", "postid": "200423509"}
        res_data = self.http_test.send_get_req(self.url, data)
        self.assertEquals(res_data["status"], "201")

# if __name__ == "__main__":
#     unittest.main()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(KuaidiInfoTest("test_type_null"))
    suite.addTest(KuaidiInfoTest("test_postid_null"))

    runner = unittest.TextTestRunner()
    runner.run(suite)

#如果执行报错，需要替换一下目录中的
# D:\Program Files (x86)\JetBrains\PyCharm 2016.3\helpers\pycharm
# utrunner.py文件