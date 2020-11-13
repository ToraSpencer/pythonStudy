# python中的宏函数
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')




# numpy, matplotlib
import matplotlib.pyplot as plt  # matplotlib是一个第三方绘图类；pyplot是一个接口类，提供了matlab风格的一些绘图接口。
plt.style.use('seaborn-whitegrid')
import numpy as np
from mpl_toolkits import mplot3d  # 导入mplot3d工具包，激活三维绘图功能。
from selfDefined import Quaternion


'''读取OBJ文件数据'''
import os


# 局部坐标系下的颌数据
objFilePath = 'E:\\jawOut.obj'
with open(objFilePath) as file:
    points = []
    while 1:
        line = file.readline()
        if not line:
            break
        strs = line.split(" ")
        if strs[0] == "v":
            points.append((float(strs[1]), float(strs[2]), float(strs[3])))
        if strs[0] == "vt":
            break






# 生成一个椭圆曲线
import math
a = 10
b = 6
N = 300
theta = 2*math.pi*np.random.rand(N)
x = a*np.cos(theta)
y = b*np.sin(theta)


# 加高斯噪声——每个点在半径为r的范围内抖动。
r = np.random.randn(N)
theta2 = 2*math.pi*np.random.rand(N)
deltax = np.multiply(r, np.cos(theta2))
deltay = np.multiply(r, np.sin(theta2))
x = x+deltax
y = y+deltay

# 椭圆逆时针旋转pi/6的角度，然后沿着向量（4，5）平移
x1 = x*np.cos(math.pi/6)-y*np.sin(math.pi/6)
y1 = x*np.sin(math.pi/6)+y*np.cos(math.pi/6)
x1 = x1+4*np.ones(N)
y1 = y1+5*np.ones(N)


x1 = x1.tolist()
y1 = y1.tolist()



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





