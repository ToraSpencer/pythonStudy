
''' pycharm快捷键'''
"""
    折叠所有代码      shift + ctrl + -
    展开所有代码      shift +ctrl + +
    注释/反注释选定行        ctrl + /
"""


''' 暂时不知道如何分类'''
print(type(3.14))       # type()——获取变量类型


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



