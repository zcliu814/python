#创建一个dog类，存储名字和年龄，并会蹲下和打滚
#类中的函数称为方法
class Dog():
	def __init__(self, name, age):  #init 两边各有两个下划线 且self必带
		"""初始化name和age"""
		self.name = name
		self.age = age
		
	def sit(self):
		print(self.name.title() + " is now sitting.")
	
	def roll_over(self):
		print(self.name.title() + " rolled over.")


class Car():
	def __init__(self, name, module ,year):
		self.name = name
		self.module = module
		self.year = year
		self.order = 'allen'  #若为方法内的属性提供初始值，则可以不设置其形参
	def show_info(self):  #self很重要 类内初始化 全用self.参数名 = 参数名 
		car_info = self.name + " " + self.module + " " + str(self.year) 
		return car_info   #赋值给变量 则是 变量名 = self.参数名
		
				
my_dog = Dog('kate', 6)
#访问实例的属性 实例名.属性名 如my_dog.name
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age))

#调用方法   实例名.方法名
my_dog.sit()
my_dog.roll_over()	

my_car = Car('audi', 'A4', 2022 )
print(my_car.show_info())

#修改属性值  句点法
my_car.name = 'alice'
print(my_car.show_info())
