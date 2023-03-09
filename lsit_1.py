name = ['bob', 'allen', 'zeka', 'sam']

#永久正序、逆序
name.sort()
print(name)

name.sort(reverse = True)
print(name)


#临时输出正序 原列表顺序不变
girl = ['lingling', 'amei' , 'huahua', 'mengmeng']

print(sorted(girl))
print(girl)


#常用列表方法
num = [1,2,3,4,5]


num.reverse() #翻转
print(len(num))      #求长度 只有len(list)不会输出 需要打印
print(num)
print(num[-1]) #输出最后一个元素 从左向右是0开始，从右向左是-1 




