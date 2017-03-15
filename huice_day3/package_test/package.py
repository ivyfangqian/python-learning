# -*-coding:utf-8-*-

# 1、为平坦的名称空间加入有层次的组织结构
# 2、允许程序员把有联系的模块组合到一起
# 3、允许分发者使用目录结构而不是一大堆混乱的文件
# 4、帮助解决有冲突的模块名称

#
import test.CurrencyConverter as cc

print cc.rmb2dollar(1000)