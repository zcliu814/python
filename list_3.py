#处理列表中的元素--切片 输出到后面索引-1

name = ['zhao', 'qian', 'sun', 'li']
print(name[0:2])  #从0开始 输出到下标1 最后一个2不输出 类似range()函数


print(name[:2])   #没有指定前面 默认从第一个开始
print(name[1:])   #没有指定后面 默认输出到结尾

#输出后两个元素 
print(name[-2:]) # 输出到结束位置


#for循环遍历切片
for names in name[1:]:
	print(names)

#复制切片列表
my_name = name[:]  #两边都不写 表示整个表
print(my_name)
