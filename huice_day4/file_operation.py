# -*-coding:utf-8-*-

# python打开文件
# 首先使用open()函数打开一个文件，创建一个file对象
# 语法
# file_object = open(name[, mode][, buffering])

file_test = open('D:\\test\\test.txt')

# 读取文件内容
print file_test.read()

file_test.close()

# 关闭后再次读取会报错
# file_test.read()


# 如何向文件中写入内容
# file_test = open('D:\\test.txt')
# 需要以写入模式打开文件
file_test = open('D:\\test\\test.txt', 'w')

# 向文件中写入内容
file_test.write('你好')

file_test.close()

# 以读的方式打开一个不存在的文件会报错
# file_test = open('D:\\test\\new.txt')

# 以写的方式打开一个不存在的文件会？？？
file_new = open('D:\\test\\new.txt', 'w')
file_new.write('Hello python')
file_new.close()

# 以写的方式打开文件，文件会被清空
file_new = open('D:\\test\\new.txt', 'w')
file_new.close()

# Python文件打开方式，有w,r,a,w+,r+,a+：
# r ： 以只读方式打开文件，文件不存在则出错
# w：以只写方式打开文件，文件存在则清空，不存在则建立
# a：以追加只写的方式打开，不清空文件，在文件末尾加入内容
# r只有读的权限，w和a只有写的权限，w清空文件，a不清空文件。（read, write,append）
# w+读写权限打开文件，只要打开就会清空文件,文件不存在则创建文件
# r+读写权限打开文件，如果写入了数据则会清空文件,文件不存在出错
# a+读写权限打开文件，不清空文件,在文件末尾新增写入的内容，文件不存在创建文件

file_new = open('D:\\test\\new.txt')

print file_new.name
print file_new.mode
print file_new.closed

file_new.close()
print file_new.closed

# 务必要调用f.close()来关闭文件。
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，
# 而是放到内存缓存起来，空闲的时候再慢慢写入。
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
# 忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。

# readline()：从文本中读取一行文本，该函数返回一行的文本字符串，包括换行符“\n”。
# read()：返回文件中剩余的文本组成的多行字符串，s
# 若打开文件时调用则返回文件中的所有内容（即使用read()之前没有使用readline()）
# readlines()：返回由文件中剩余的文本（行）组成的列表,  遍历返回的列表即可得到每一行的内容。
# write()
# writelines(list)
# truncate([size])
# flush(),一般的文件流操作都包含缓冲机制，write方法并不直接将数据写入文件，而是先写入内存中特定的缓冲区。
# flush方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区。


# 对文件系统的访问主要通过os模块来进行，os模块主要用于访问操作系统命令
# import os
# os.rename('file.txt','file-new.txt') 文件重命名
# os.remove('file-new.txt') 删除文件
# os.mkdir('test') 创建文件夹
# os.rmdir('test') 删除文件夹
# os.sep 可以取代操作系统特定的路径分割符
# os.getcwd() 相当于Linux下的pwd，获取当前目录
# os.chdir(os.getcwd()+os.sep+'test') 进到某个目录下
# os.listdir(os.getcwd()) 相当于Linux下的ls，显示当前目录下的文件
# os.path.isfile("test.txt") 判断是否是文件
# os.path.isdir("test.txt") 判断是否是文件夹
# os.path.exists("test.txt") 判断文件是否存在
# os.path.getsize("test.txt") 获取文件的大小
# os.path.abspath("test.txt") 返回文件的绝对路径
# os.path.basename(os.path.abspath("test.txt")) 获取文件的文件名，注意参数需要传入绝对路径
# os.path.dirname(os.path.abspath("test.txt")) 获取文件的所在目录，注意参数需要传入绝对路径
import os

# os.rename('D:\\test\\test.txt','D:\\test\\test01.txt')
# os.remove('D:\\test\\hello.txt')
# os.mkdir('D:\\test\\ivy')
# os.makedirs('D:\\test\\ivy\\test')

# 实现目录递归遍历，查找以.py结尾的文件，并将文件绝对路径存入log.txt文件。
res = []

def go_through(dir):
    for i in os.listdir(dir):
        if os.path.isdir(dir + os.sep + i):
            go_through(dir + os.sep + i)
        else:
            if i[-3:] == '.py':
                res.append(dir + os.sep + i)

go_through('D:\\test')
print res

file_log = open('D:\\test\\log.txt','w+')
for i in res:
    file_log.write(i+'\n')
file_log.close()