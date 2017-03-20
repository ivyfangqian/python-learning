# -*-coding:utf-8-*-

import xlrd

# 使用xlrd模块对excel文件进行读操作

# 打开一个excel文件
wkb = xlrd.open_workbook('D:\\test\\test.xlsx')

# excel中所有的sheet的名字
print wkb.sheet_names()

sheet = wkb.sheets()[0]
wkb.sheet_by_index(0)
wkb.sheet_by_name('Sheet1')

# sheet的行数
print sheet.nrows

# sheet的列数
print sheet.ncols

# sheet的一行的值
print sheet.row_values(0)

# sheet一列的值
sheet.col_values(0)

# 取第一行第二列的值
print sheet.cell(0,1).value

print sheet.cell_value(0,1)

print sheet.row(0)[1].value

print sheet.col(1)[0].value

# 使用xlwt模块进行写操作
import xlwt

wkbw = xlwt.Workbook()

# 添加sheet
sheetw = wkbw.add_sheet('Sheet1',cell_overwrite_ok=True)

# 写入单元格内容
sheetw.write(0,1,'hello python')
sheetw.write(0,1,'hello huice')
sheetw.write(0,0,18)

# 设置格式
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True

style.font = font
style2 = xlwt.easyxf('pattern:pattern solid,fore_colour red;font:bold on;')
sheetw.write(0, 0, 'leili', style)
sheetw.write(0, 1, 18, style2)

# 保存文件
wkbw.save('D:\\test\\test01.xls')

# excel修改操作
from xlutils import copy

# 打开文件
wkb_rd= xlrd.open_workbook('D:\\test\\test01.xls')

# 进行拷贝
wkb_cp = copy.copy(wkb_rd)

# 获取sheet
sheet = wkb_cp.get_sheet(0)

# 写入内容
sheet.write(1,0,'hanmeimei')
sheet.write(1,1,16)

# 保存文件
wkb_cp.save('D:\\test\\test01.xls')