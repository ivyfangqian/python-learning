# -*-coding:utf8-*-

import unittest
from HTMLTestRunner import HTMLTestRunner
import time

test_dir = "./interface"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")

if __name__ =="__main__":
    now = time.strftime("%Y%m%d%H%M%S")
    filename = "d:\\test\\res\\res"+now+".html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner(fp,title=u"接口测试报告",description=u"接口测试用例实例")
    runner.run(discover)
    fp.close()