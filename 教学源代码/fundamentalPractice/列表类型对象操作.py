#创建列表，并且循环输出列表元素
list = [1,2,3,4,5]
print("list all the elements in the list:")
for i in list:
    print(i)
print('\n')
    
print("is 2 in the list?")
print(2 in list)
print("is 8 in the list?")
print(8 in list)
print('\n')

list.append('python')
print("list all the elements in the list:")
for i in list:
    print(i)
print('\n')

list.reverse()
print("list all the elements in the list:")
for i in list:
    print(i)
print('\n')
