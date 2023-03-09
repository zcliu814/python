#简单的if条件语句

name = ['zhao', 'qian', 'sun', 'li',]
age_1 = 16;age_2 = 18;age = 17

if age > 16 and age < 18:   #and语句
	print("Yes")
else:
	print("No")

if age < 16 or age >18:     #or语句
	print("Yes")
else:
	print("No")


if 'zhao' in name:          #in和not in 判断特定值是否在列表中
	print("Yes")
if 'qi' not in name:
	print("Not")



# if-elif-else 检查超过两个条件的语句,满足任何一个立即终止下面的测试
#设置条件 14岁以下基本不能参加，14-16岁或许可以参加，18岁以上肯定可以参加、
age = 15
if age < 14:
	print("Good Bye")
elif age < 16:
	print("Maybe")
else:
	print("Welcome")
	

#ps 多个条件无论是否满足都要测试时  采用多个if语句即可


#检查列表是否为空
boy = []
if boy:               #判空语句
	print("No")
else:
	print("Yes")


#最终测试  店里提供3种瓜，东南西，如果顾客来买，有则输出拿好您的瓜，没有则输出你是不是来找茬啊

provide = ["南瓜","西瓜","东瓜"]
consumer_1 = ["南瓜","西瓜"]
consumer_2 = ["北瓜"] 

for consumers in consumer_1:
	if consumers in provide:
		print("拿好您的瓜")
	else:
	    print("是不是来找茬啊")

for consumers in consumer_2:
	if consumers in provide:
		print("拿好您的瓜")
	else:
	    print("是不是来找茬啊")
