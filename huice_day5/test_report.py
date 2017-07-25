# -*-coding:utf8-*-

import unittest
import requests_test
from HTMLTestRunner import HTMLTestRunner
import time

class KuaidiInfoTest(unittest.TestCase):
    url = "http://www.kuaidi100.com/query"

    def setUp(self):
        self.http_test = requests_test.HttpRequestTest()

    def tearDown(self):
        pass

    def test_type_null(self):
        data = {"type": "", "postid": "200423509764"}
        res_data = self.http_test.send_get_req(self.url, data)
        self.assertEquals(res_data["status"], "400")

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
        self.assertEquals(res_data["status"], "200")


# if __name__ == "__main__":
#     unittest.main()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(KuaidiInfoTest("test_type_null"))
    suite.addTest(KuaidiInfoTest("test_postid_null"))
    suite.addTest(KuaidiInfoTest("test_type_error"))
    suite.addTest(KuaidiInfoTest("test_postid_error"))

    html_file = "d:\\test\\res"+ time.strftime("%Y%m%d%H%M%S") +".html"
    fp = file(html_file,"wb")
    runner = HTMLTestRunner(fp,title=u"快递信息测试报告",description=u"接口用例测试情况")
    runner.run(suite)
