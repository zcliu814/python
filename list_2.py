names = ['allen', 'bob', 'sam', 'doctor']

#for循环遍历 把列表names的一个元素存到临时变量name中，打印一个，再次循环第二个
for name in names:
	print(name)
	


#数值列表

for value in range(1,6):  #range()方法生成一个顺序数列，不包含最后一个数字
	print(value)


numbers = list(range(1,7))  #list()方法将range()结果转化为列表
print(numbers)     


even_numbers = list(range(1,11,2)) #range()指定步长 从1到10 步长为2 
print(even_numbers)                #可用于打印奇数偶数


#打印平方1-10存到列表
squares = []
for value in range(1,11):
	squares.append(value**2) #循环添加 最后缩进输出
print(squares)

#列表解析 更少的代码完成输出平方项  for循环更简单输出列表
squares_1 = [value_1**2 for value_1 in range(1,11)]
print(squares_1)


#常用数字函数 需要打印才能输出
print(str(min(squares)) + " " + str(max(squares))  + " " + str(sum(squares)))
'''
str()函数把数字转化为字符串，否则+会把数值相加输出
'''


