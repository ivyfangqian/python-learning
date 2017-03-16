#-*-coding:utf-8-*-

# 类的私有属性与方法
# 默认情况下，python中属性都是公开的，可以直接访问
# 私有属性：__private_attr，以双下划綫开头
class JustCounter:
	__secretCount = 0  # 私有变量
	publicCount = 0    # 公开变量

	def count(self):
		self.__secretCount += 1
		self.publicCount += 1
		print self.__secretCount

	def get_secret_count(self):
		return  self.__secretCount
	def set_secret_count(self,num):
		self.__secretCount = num
		return  self.__secretCount
	def __print_info(self):
		print '私有方法'

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
print '----------------------'
# print counter.__secretCount  # 报错，实例不能访问私有变量
# counter.__print_info()

# python使用的是名字重整的技术，改变了私有变量的值：_类名__变量名
# 如果我们一定要访问私有变量的话
print counter._JustCounter__secretCount #虽然可以，但是我们并不推荐使用这种方法
print counter.get_secret_count()

# 先用set方法赋值，再用get取值
counter.set_secret_count(5)
print counter.get_secret_count()



class Test(object):
	def object_test(self):
		print 'object method'

	@classmethod
	def class_test(cls):
		print 'class method'

	# 要在类中使用静态方法，需在类成员函数前面加上 @ staticmethod标记符，
	# 以表示下面的成员函数是静态函数。
	# 使用静态方法的好处是，不需要定义实例即可使用这个方法。
	# 另外，多个实例共享此静态方法。
	@staticmethod
	def static_test():
		print 'static method'

# 调用实例方法
test1 = Test()
test1.object_test()
Test.object_test(test1)

# 调用类方法
test1.class_test()
Test.class_test()

# 调用静态方法
test1.static_test()
Test.static_test()

# 继承父类Test，继承父类的属性和方法
class SubTest(Test):
	# 对父类方法的覆盖
	@classmethod
	def class_test(cls):
		print cls
		print 'subclass method'

# 调用子类的类方法
SubTest.class_test()

# 调用父类中的其他方法
subTest = SubTest()
subTest.object_test()
SubTest.object_test(subTest)
SubTest.static_test()


# 类的继承
class A(object):
	pass

class B(object):
	pass

class C(A):
	pass

class D(B,C):
	pass

print A.__bases__
print B.__bases__
print C.__bases__
print D.__bases__

