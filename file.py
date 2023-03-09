#读取程序目录内文件life.txt内容
with open('life.txt') as file_object:  #打开文件地址 返回一个表示文件的对象 存储到变量file_object中
	contents = file_object.read() #read()函数读取变量file_object存到字符串contents中
	print(contents)
	
#读取任意位置目录文件
file_path = 'D:\.GitCode\Python\Geany\python_work\life.txt'
with open(file_path) as file_object:
	contents = file_object.read() 
	print(contents)

with open(file_path) as file_object:  #逐行读取
	for line in file_object:
		#print(line)               #print会输出空行 而rstrip()消除段尾空行 空格
		print(line.rstrip())

# strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
#rstrip() 删除 string 字符串末尾的指定字符，默认为空白符，包括空格、换行符、回车符、制表符

print("\n")
#使用with关键字打开的文件 只能在with的代码块中使用 要想在之外使用 使用readllinse()
#函数即可 他会把文件对象的内容存储在一个列表中
with open(file_path) as file_object:  
	lines = file_object.readlines()   

life_string = ''	#字符串		
for line in lines:
	#print(line)
	life_string += line.rstrip() + " "  #削除换行符 使字符串连接成一行
	#print(line.rstrip())  #在with之外输出文件内容（不带空行）
print(life_string)
print(life_string[:4])  #输出前四个字符
	
	
#文件写入
file_name = 'test.txt'
with open(file_name, 'w') as file_object:  #r读取，w写，a附加，r+读写，省略则默认只读
	file_object.write("I love programming\n")
	file_object.write("I love programming!\n")
	
	
#write()不会添加换行符 写入多行需要自己添加换行符

#写入会覆盖原有内容 要覆盖在结尾添加采用附加模式
with open(file_name, 'a') as file_object:  #r读取，w写，a附加，r+读写，省略则默认只读
	file_object.write("I love programming!!\n")
	file_object.write("I love programming!!!\n")
#使用写入模式时，无法读取文件 要么去文件自己看 要么使用r+ 或者w+

