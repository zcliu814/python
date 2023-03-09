#传递实参

#1 位置实参  按顺序传参

def pet(pet_name, pet_age=100): #形参指定默认值 等号=两边不要有空格
	print("\nThis is a " + str(pet_name)) #5是数值 要转化为字符串才能用加号+
	print("\nIts age is " + str(pet_age))

pet('dog', 5)
pet(5,'dog')


#关键字实参  直接传值 不用考虑顺序 形参名要写对
pet(pet_age=6, pet_name='cat')  #关键字实参 等号两边不要有空格

#默认值 形参若指定默认值，调用时相应实参为空则采用默认值输出
pet('alice')


#可选择的实参输入 函数中把可选可不选的形参设置为空即可
#人名中 中间名可有可无 是可选择的实参
def get_name(first_name, last_name, middle_name = ""):#有默认值的参数要放最后面
	if middle_name: #更精确的输出 非必须
		full_name = first_name + " " + middle_name + " " + last_name
	else:
		full_name = first_name + " " + last_name
	return full_name.title()

name = get_name('liu', 'hua', 'de')
print(name)
name = get_name('liu', 'hua')	
print(name)

#有关函数列表 将第一个列表传输到第二个  用切片可以不改变第一个表


def transport (first_list, second_list):
	while first_list:
		transporting = first_list.pop()
		second_list.append(transporting)
	for second in second_list:
		print(second)
			
first_list = ["zhao", "qian", "sun", "li"]
second_list = []

transport(first_list[:], second_list) #用切片使用的是副本不会改变第一个列表 [:]
print(first_list)
'''
transport(first_list, second_list)
print(first_list) #此时第一个列表弹出所有元素  要想不改变第一个列表完成传输 用切片

'''
