#继承  几乎固定搭配  类内方法必有形参self
class Car():
	def __init__(self, name, module):
		self.name = name 
		self.module = module
		
	def show_info(self):
	    
		print("This is a car: " + self.name + " " + self.module)
		
class ElectricCar(Car): #继承Car类
	def __init__(self, name, module):
		super().__init__(name, module)  #super()联系父类和子类
		self.battery = 70 #设置子类特有属性
	
	def battery_capacity(self):
		print("This is " + str(self.battery) + " battery car")
		
	def show_info(self): #重写父类方法shoe_info() 子类会执行子类的方法 忽略父类同名方法
	    
		print("This is a battery car: " + self.name + " " + self.module)

my_car = Car('audi', 'A4')
my_ecar = ElectricCar('xiaoniao', 'F4')

my_car.show_info()  #父类执行父类方法
my_ecar.show_info()  #重写后执行子类方法  不重写执行父类同名方法
my_ecar.battery_capacity()



	
