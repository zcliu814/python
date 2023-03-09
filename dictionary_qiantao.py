'''

嵌套 
有时候需要将字典存储在列表中，或者将列表作为值存在字典中  可以互相嵌套
甚至在字典中嵌套字典

'''

#字典alien包含一个外星人的信息，但无法存储第二个外星人的信息，想要管理多个外星人信息，
#可以创建一个外星人队列，其中每个外星人都是一个字典。


#列表中存储字典
alien_0 = {'color': 'blue' , 'points': '5'}
alien_1 = {'color': 'yellow' , 'points': '50'}
alien_2 = {'color': 'bred' , 'points': '500'}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)
	
for alien in range(3):  #range()配合for循环3次数
	print("yes")


#字典中存储列表-->一个键关联多个值
#每个人和喜欢的女孩
relation = {
	'allen': ['lingling', 'mengmeng', 'lili'], #,不要省略
	'bob': ['tongtong', 'huahua'],
	'sam': ['alice'],
	}
	
	# 把名字键存入name ,对应的多个键值存入girls 因此name输出不需要遍历 girls需要
for name,girls in relation.items():
	print("\n" + name.title() + "'s favorite girl is:")
	for girl in girls:
		print("\t" + girl.title()) 
	

#字典存入字典 
#例如字典是不同用户  每个用户包括名字 性别 住址三个信息

users = {
	'allen': {
		'love': 'alice',
		'sex': 'male',
		'address': 'shandong',
		},  #字典两个键之间的逗号 别忽略了
		
	'alice': {
		'love': 'allen',
		'sex': 'female',
		'address': 'beijing',
		},  
	}
		
#for循环输出名字 跟着三个信息
for name, infos in users.items():
	print("\nUsername is : " + name)
	print("\tLove is " + infos['love'])
	print("\tSex is " + infos['sex'])
	print("\tAddress is " + infos['address'])
