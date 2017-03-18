# -*-coding:utf-8-*-

# 美元换算为人民币
def dollar2rmb(dollar):
    rmb = dollar * 6.9130
    return rmb

def rmb2dollar(rmb):
    dollar = rmb / 6.9130
    return dollar

class A():
    def hello(self):
        print 'Hello python!'