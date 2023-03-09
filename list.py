#这是列表练习
list = ['I', 'am', 'a', 'good' ,'boy']


#输出列表
print(list)
print(list[1])


#修改
list[0] = 'your'
print(list[0]) 


#添加
list.append('?') #默认添加到末尾
list.insert(0,'but') #插入
print(list)


#删除

del list[5] #按下标删除
list.remove('am') #按值删除第一个 此函数较为麻烦 若原列表发生改动 会报错 慎用

#删除并弹出
name = list.pop(0)
print(name)
print(list)





