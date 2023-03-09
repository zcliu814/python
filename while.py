# 不停输入 直到quit时候退出
prompt ="\nTell me something , and I will repeat to you."
prompt +="\nEnter 'quit' to exit:"

message =""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':   #此处防止输入的quit也被输出
		print(message)
	
#break 和continue


#while()处理字典和列表
#v创建一个问卷调查 符合条件则继续循环 不符合则结束循环

responses = {}

#标志  指出调查是否继续
mark = True;
while mark:
	#输入被调查者的名字和回答
	name = input("\nWhat's your name? ")
	response = input("Who do you like ? ")
	
	#将答案存在字典中
	responses[name] = response   #字典创立格式  键为name 值为responses 均为上文输入
	
	answer = input("Have you anotther word to say? (yes or no)")
	answer = answer.lower()  #全变小写
	if answer == 'yes':
		print("Welcome to again!")
	else:
		mark = False   #标记为false 终止循环
			
for name,response in responses.items():  #标准字典循环输出格式
	print(name + "'like is " + response + ".")
	print(responses)
