
''' pycharm快捷键'''
"""
    折叠所有代码      shift + ctrl + -
    展开所有代码      shift +ctrl + +
    注释/反注释选定行        ctrl + /
"""


# 注释

"""
    多行注释
"""
''' 单行注释'''
# 单行注释

''' 暂时不知道如何分类'''
print(type(3.14))       # type()——获取变量类型


''' 导入模块、函数'''
"""
    import timeit           # 导入整个模块
    print(timeit.Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
    import numpy as np      # 导入整个模块并设置别名
    from math import pi     # 从模块中导入单个数据、函数，则使用的时候不需要模块名前缀
    from math import *      # 想要导入整个模块又懒得用别名就这样。
    print(pi)
"""


''' 基本语句'''
"""
    if-else条件分支 
        age = int(input("请输入你家狗狗的年龄: "))
        print("")
        if age <= 0:
            print("你是在逗我吧!")
        elif age == 1:
            print("相当于 14 岁的人。")
        elif age == 2:
            print("相当于 22 岁的人。")
        elif age > 2:
            human = 22 + (age - 2) * 5
            print("对应人类年龄: ", human)
        else:
            print("错误")



    while循环 
        n = 100
        sum = 0
        counter = 1
        while counter <= n:
            sum = sum + counter
            counter += 1
        print("1 到 %d 之和为: %d" % (n, sum))


    for循环 
        sites = ["Baidu", "Google", "Runoob", "Taobao"]
        for site in sites:
            if site == "Runoob":
                print("菜鸟教程!")
                break
            print("循环数据 " + site)
        else:
            print("没有循环数据!")
        print("完成循环!")


    for循环中使用range()函数 
        for i in range(5, 9):
            print(i)
        
        for i in range(-10, -100, -30):
            print(i)
"""


''' python中的逻辑运算符是and, or, not'''


'''数据类型'''
"""
    整形
            Python3 整型是没有限制大小的
    浮点型
            可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
    复数
            表示：a + bj， 或complex(a, b)
            实部虚部都是浮点类型
    
    字符串
            可以使用引号( ' 或 " )来创建字符串。
            Python不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
            字符串格式化
                    类似C的语法
                    例：print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

    
"""


''' list类型'''
"""
    创建
        方括号+逗号
    
    接口——增删查改：
        append()方法
            在尾部追加元素
            
        insert()方法
            在任意位置插入元素
            
        pop()方法
            弹出元素
        
        remove()方法
            删除某个值的元素
        
        del关键字删除元素
            例：del arr[0]
    
    接口——组织结构：
        sort()方法
        sorted()
        reverse()方法
        len()
        
    
        
    
    
    



"""


''' 常用数学接口'''
"""
    import math
        导入数学库
    
    数学常量
        pi	
        e	
         
    随机数
        choice(seq)	
                从序列的元素中随机挑选一个元素
                例；random.choice(range(10))，从0到9中随机挑选一个整数。
                
        randrange ([start,] stop [,step])	
                从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
        
        random()	
                随机生成下一个实数，它在[0,1)范围内。
        
        seed([x])	
                改变随机数生成器的种子seed。
                如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
        
        shuffle(lst)	
                将序列的所有元素随机排序
        
        uniform(x, y)	
                随机生成下一个实数，它在[x,y]范围内。
            
    三角函数
            acos(x)	
                    返回x的反余弦弧度值。
            asin(x)	
                    返回x的反正弦弧度值。
            atan(x)	
                    返回x的反正切弧度值。
            atan2(y, x)	
                    返回给定的 X 及 Y 坐标值的反正切值。
            hypot(x, y)	
                    返回欧几里德范数 sqrt(x*x + y*y)。
            degrees(x)	
                    将弧度转换为角度,
                    如degrees(math.pi/2) ， 返回90.0
            radians(x)	
                    将角度转换为弧度
    
"""


''' 常用标准库'''
"""
    操作系统接口os
    文件通配符glob
    命令行参数sys
    数学库math
    正则表达式库re
    字符串-二进制数据转换工具struct
    
    
    sys库
        getsizeof()
                获取对象占内存空间的字节数。
                
    
"""


''' 文件读写'''
"""
    import struct
    import os
    arr = []
    for i in range(10):
        arr.append(i)
    
    
    with open("data.dat", 'wb') as f:           # wb模式表示二进制写模式
        for elem in arr:
            s = struct.pack('d', elem)          
            f.write(s)
        f.close()
    
    
    num = []
    with open("data.dat", 'rb') as f:           # rb模式表示二进制读模式
        size = os.path.getsize('data.dat')      # os.path.getsize()方法获取文件大小
        size = int(size/8)              
        for i in range(size):
            data = f.read(8)                    # 指定每次读8个字节——一个double的长度
            arg = struct.unpack('d', data)      # 指定解包的格式是一个double类型的数据
            num.append(arg[0])                  # unpack出来的数据是一个元祖。
        f.close()
    print(num)

"""


''' 调用自己写的轮子来读取.dat文件中的数组'''
""" 
import struct
with open("x.dat", 'wb') as file:
    for elem in x1:
        temp = struct.pack('d', elem)
        file.write(temp)
    file.close()

with open("y.dat", 'wb') as file:
    for elem in y1:
        temp = struct.pack('d', elem)
        file.write(temp)
    file.close()


xx = []
yy = []
with open('x.dat', 'rb') as file:
    size = os.path.getsize('x.dat')
    size = int(size/8)
    for i in range(size):
        temp = file.read(8)
        temp = struct.unpack('d', temp)
        xx.append(temp[0])
    file.close()


with open('y.dat', 'rb') as file:
    size = os.path.getsize('y.dat')
    size = int(size/8)
    for i in range(size):
        temp = file.read(8)
        temp = struct.unpack('d', temp)
        yy.append(temp[0])
    file.close()


fig = plt.figure()
ax = plt.axis()
plt.plot(xx, yy, '*b')



from selfDefined import readDoubleArray
xx = readDoubleArray('x.dat')
print(xx)
"""



