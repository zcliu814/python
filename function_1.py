#不知道需要传递多少实参 用*形参 一般放在最后
def print_name(*name):
	print(name)
	
print_name("liu")
print_name("zhao", "qian", "sun", "li")

'''
p77 使用任意数量的关键字实参 没看懂 字典相关 用**形参访问键值对

def build profile(first, last, **user_info):
	profile = {}
	profile['firat_name'] = first
	profile['last_name'] = lsst
	for key,vlaue in user_info.items():
		profile[key] = value
	return proffile
user_profile = build_profile('allen', 'sam'
								localion ='linqing',
								field = 'physics')
print(user_profile)
	
'''

#导入模块 同一目录内 调用function_module函数tell()
import function_module #导入全部函数
function_module.tell('allen')       #格式  模块名.函数名
import function_module as module     #给模块别名 更容易应用
module.tell('me')


#导入特定函数
# for 模块名 import 函数名1，函数名2，
#如要从上个模块只导入一个tell函数 
from function_module import tell
tell('zhao')                        #格式 直接用函数名 不再需要模块名.函数名、

#给导入的函数值指定别名 防止和现有程序的冲突
from function_module import tell as tell_me  #可以用tell_me代替tell了
tell_me('girls')


#导入模块所有函数
from function_module import *  
#尽量只用用官方模块 使用非自己编写的大型模块时 只导入使用的具体函数
#或者使用句点表示法 主要为了清晰 
#所有import文件都应放在开头


  

