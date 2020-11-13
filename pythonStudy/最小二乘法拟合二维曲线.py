# numpy, matplotlib
# 在pycharm中使用第三方库，设置 → Python interpreter 中搜索第三方库，然后install
import matplotlib.pyplot as plt         # matplotlib是一个第三方绘图类；pyplot是一个接口类，提供了matlab风格的一些绘图接口。
plt.style.use('seaborn-whitegrid')
import numpy as np
from mpl_toolkits import mplot3d            # 导入mplot3d工具包，激活三维绘图功能。


'''拟合直线'''
# 生成带有噪点的待拟合的数据集合
x = np.arange(0, 10, 0.1)
y = 2*x+1
y = y + 2*np.random.rand(100)
N = 100


fig = plt.figure()
ax = plt.axis()
plt.plot(x, y, '*b')


A11 = sum(np.multiply(x, x))
A12 = sum(x)
A21 = sum(x)
A22 = -N
b1 = sum(np.multiply(x, y))
b2 = sum(y)

A = np.array([[A11, A12], [A21, A22]])
b = np.array([b1, b2])
b = b.reshape(2, 1)
X = np.matmul(np.linalg.inv(A), b)
print(X)

x1 = x
y1 = X[0][0]*x+ X[1][0]
plt.plot(x1, y1, color='red')
plt.show()


'''拟合椭圆曲线'''
# 生成一个椭圆曲线
a = 10
b = 6
pi = 3.14159
N = 300
theta = 2*pi*np.random.rand(N)
x = a*np.cos(theta)
y = b*np.sin(theta)


# 加高斯噪声——每个点在半径为r的范围内抖动。
r = np.random.randn(N)
theta2 = 2*pi*np.random.rand(N)
deltax = np.multiply(r, np.cos(theta2))
deltay = np.multiply(r, np.sin(theta2))
x = x+deltax
y = y+deltay

# 椭圆逆时针旋转pi/6的角度，然后沿着向量（4，5）平移
x1 = x*np.cos(pi/6)-y*np.sin(pi/6)
y1 = x*np.sin(pi/6)+y*np.cos(pi/6)

x1 = x1+4*np.ones([1, N])
y1 = y1+5*np.ones([1, N])

x = x1
y = y1

fig = plt.figure()
ax = plt.axis()
plt.plot(x, y, '*b')


def mmulti3(a, b, c):
    temp = np.multiply(a,b)
    temp = np.multiply(temp, c)
    return temp

def mmulti4(a, b, c, d):
    temp = np.multiply(a, b)
    temp = np.multiply(temp, c)
    temp = np.multiply(temp, d)
    return temp

def sum3(a, b, c):
    temp = np.sum(mmulti3(a,b,c))
    temp = float(temp)
    return temp

def sum4(a,b,c,d):
    temp = np.sum(mmulti4(a,b,c,d))
    temp = float(temp)
    return temp

def sum2(a,b):
    temp = np.sum(np.multiply(a,b))
    temp = float(temp)
    return temp

def sum1(a):
    temp = np.sum(a)
    temp = float(temp)
    return temp


# 椭圆方程设为x^2+Bxy+Cy^2+Dx+Ey+F = 0
A = [[sum4(x,x,y,y), sum4(x,y,y,y), sum3(x,x,y), sum3(x,y,y), sum2(x,y)],
            [sum4(x,y,y,y), sum4(y,y,y,y), sum3(x,y,y),sum3(y,y,y), sum2(y,y)],
            [sum3(x,x,y), sum3(x,y,y), sum2(x,x), sum2(x,y), sum1(x)],
            [sum3(x,y,y), sum3(y,y,y), sum2(x,y), sum2(y,y), sum1(y)],
            [sum2(x,y), sum2(y,y), sum1(x), sum1(y), float(N)]]
b = [sum4(x,x,x,y), sum4(x,x,y,y), sum3(x,x,x), sum3(x,x,y) , sum2(x,x)]
b = np.array(b)
b = -b
b = b.reshape([5, 1])


X = np.matmul(np.linalg.inv(A), b)
B = X[0]
C = X[1]
D = X[2]
E = X[3]
F = X[4]
print(X)




x0 = np.linspace(-10, 10, 100)
y0 = x0
x,y = np.meshgrid(x0,y0)
z= x**2+C*y**2+B*x*y+D*x+E*y
z=z.reshape(x.shape)#z数组的大小必须和xx,yy大小一致
plt.contour(x, y, z, [0, -F])
plt.show()

