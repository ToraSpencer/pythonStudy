# numpy, matplotlib
# 在pycharm中使用第三方库，设置 → Python interpreter 中搜索第三方库，然后install
import matplotlib.pyplot as plt         # matplotlib是一个第三方绘图类；pyplot是一个接口类，提供了matlab风格的一些绘图接口。
plt.style.use('seaborn-whitegrid')
import numpy as np
from mpl_toolkits import mplot3d            # 导入mplot3d工具包，激活三维绘图功能。






# 以直线l1: y = x+1为PCA1, 直线l2: y = -x+5为PCA2做一组xoy平面上的数据点，均值点应该为(2,3)

#   1. 先在a = 100,b = 30的椭圆区域上生成1000个随机的数据点。
np.random.seed(1234)        #设置随机种子为1234
theta = 2*3.14159*np.random.rand(1, 1000)
scale = np.random.rand(1, 1000)
a = 100
b = 30
x = a*np.cos(theta)*scale
y = b*np.sin(theta)*scale



# 所有数据点逆时针旋转pi/6，然后沿着向量(2,3)平移
pi = 3.14159
x1 = x*np.cos(pi/6)-y*np.sin(pi/6)
y1 = x*np.sin(pi/6)+y*np.cos(pi/6)

x1 = x1+2*np.ones([1,1000])
y1 = y1+3*np.ones([1,1000])
z1 = np.random.rand(1, 1000)


# 这样生成的数据点(x1,y1)应该满足要求，接下来用主成分分析算法求出PCA1和PCA2，看看是否接近预设的两条直线。


fig1 = plt.figure()

ax1 = plt.axis()
plt.plot(x1, y1, '*b')
plt.show()

# 生成样本矩阵
A = np.hstack([x1.reshape([1000, 1]), y1.reshape([1000, 1]),z1.reshape([1000,1])])     # 每行为一个样本，每列为一个随机变量。
miu = np.sum(A, 0)/1000                     # 样本均值
B = A-np.tile(miu, [1000, 1])
C = np.matmul(np.transpose(B),B)/(1000-1)     # 样本协方差矩阵。
[lam, eigvec] = np.linalg.eig(C)            #？？？貌似是特征值越大，对应特征向量方向上的方差越大？



# 找出最大特征值，及其对应特征向量
lamlist = lam.tolist()
maxindex = lamlist.index(max(lamlist))

print(eigvec*10000)
print(lam)

# 求一下PCA1的斜率，只看xoy平面
print(eigvec[0][1]/eigvec[0][0])
print(1/np.sqrt(3))
