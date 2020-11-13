#导入random库，生成一个随机数
import random
a = random.random();
print('a random number between 0 and 1:',a)
print('\n')
#uniform函数生成一个区间内的随机浮点数，randint函数生成一个区间内的随机整数
b = random.uniform(1,10)
c = random.randint(1,10)
print('a random float between 1 and 10:',b)
print('\n')
print('a random integer between 1 and 10:',c)
print('\n')

#choice函数随机选取列表中的元素
list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
    print(i)
print('choose a element randomly from the list:',random.choice(list))
print('\n')

#shuffle函数打乱列表中的元素
random.shuffle(list)
print('show the list after shuffling:')
for i in list:
    print(i)
print('\n')

#sample函数对列表随机采样
list1 = random.sample(list,5)
print('the sample of the elements of the list is:')
for i in list1:
    print(i)
print('\n')
