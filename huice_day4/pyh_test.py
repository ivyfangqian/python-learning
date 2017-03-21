# -*-coding:utf-8-*-

from pyh import *

list = [[1, 'xiaoming', 20], [2, 'xiaohong', 21], [3, 'xiaofang', 22]]
page = PyH('Test')

page << div(style="text-align:center") << h4('Test table')

mytab = page << table(border='1', cellpadding='3', cellspacing='0', style='margin:auto')

tr1 = mytab << tr(bgbolor='lightgrey')
tr1 << th('id') + th('name') + th('age')

for i in range(len(list)):
    tr2 = mytab << tr()
    for j in range(3):
        tr2 << td(list[i][j])

page.printOut('D:\\test\\test.html')
