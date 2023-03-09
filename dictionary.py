# 字典  花括号 一个键对应一个值，值可以是数字、字符串、列表乃至字典

alien_0 = {'name': 'allen', 'sex': 'man', 'color': 'red'}
print(alien_0['color'])  #访问某键


#增
alien_0['points'] = 'blue'    #默认添加到结尾
print(alien_0)

#改
alien_0['color'] = 'blue'  
print(alien_0)

#删
del alien_0['sex']
print(alien_0)


#遍历便利字典并不一定按顺序 是无序输出)
for key,value in alien_0.items():   #items()返回一对键-值对列表 存储在key vlaue中
	print("\nThe key is " + key)
	print("The value is " + value)
	
#只遍历字典的键或者值
print("---------------------------------------------")
for key in alien_0.keys():         #keys()方法可以省略 遍历字典默认只遍历键 
	print("The Key is " + key)      #keys()返回包含所有键的列表
    
for value in alien_0.values():
	print("The vlaue is " + value)   #values()方法遍历值不删除重复 
	
	
print("---------------------------------------------")	
#若想得到不重复的值，就创建一个集合
for value in set(alien_0.values()):
	print("The value is " + value)  #set()方法可以把列表变为没有重复元素的集合

	

	
	
