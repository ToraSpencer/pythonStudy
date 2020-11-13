
    # numpy, matplotlib
    # 在pycharm中使用第三方库，设置 → Python interpreter 中搜索第三方库，然后install
    import matplotlib.pyplot as plt  # matplotlib是一个第三方绘图类；pyplot是一个接口类，提供了matlab风格的一些绘图接口。

    plt.style.use('seaborn-whitegrid')
    import numpy as np
    from mpl_toolkits import mplot3d  # 导入mplot3d工具包，激活三维绘图功能。


    class Quaternion:
        def __init__(self, s, x, y, z):
            """构造函数"""
            self.s = s
            self.x = x
            self.y = y
            self.z = z
            self.vector = [x, y, z]
            self.all = [s, x, y, z]

        def __str__(self):
            """输出操作重载"""
            op = [" ", "i ", "j ", "k"]
            q = self.all.copy()
            result = ""
            for i in range(4):
                if q[i] < -1e-8 or q[i] > 1e-8:
                    result = result + str(round(q[i], 4)) + op[i]
            if result == "":
                return "0"
            else:
                return result

        def __add__(self, quater):
            """加法运算符重载"""
            q = self.all.copy()
            for i in range(4):
                q[i] += quater.all[i]
            return Quaternion(q[0], q[1], q[2], q[3])

        def __sub__(self, quater):
            """减法运算符重载"""
            q = self.all.copy()
            for i in range(4):
                q[i] -= quater.all[i]
            return Quaternion(q[0], q[1], q[2], q[3])

        def __mul__(self, quater):
            """乘法运算符重载"""
            q = self.all.copy()
            p = quater.all.copy()
            s = q[0] * p[0] - q[1] * p[1] - q[2] * p[2] - q[3] * p[3]
            x = q[0] * p[1] + q[1] * p[0] + q[2] * p[3] - q[3] * p[2]
            y = q[0] * p[2] - q[1] * p[3] + q[2] * p[0] + q[3] * p[1]
            z = q[0] * p[3] + q[1] * p[2] - q[2] * p[1] + q[3] * p[0]
            return Quaternion(s, x, y, z)


        def rotateVec(self, v):
            '''对一个三维向量(shape:[3, ])施加旋转操作'''
            vq = self.vector
            a = np.cross(vq, v)
            b = np.cross(vq, a)
            a = 2 * q.s * a
            b = 2 * b
            result = v+a+b
            return result






# 读取OBJ文件数据
import os

objFilePath = 'E:\\testdata\\jawMeshUpper.obj'
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

# points原本为列表，需要转变为矩阵，方便处理
points = np.array(points)


[x, y, z] = np.hsplit(points, 3)


fig3 = plt.figure()
ax3 = plt.axes(projection='3d')          # 关键字参数projection='3d'指定创建维度为三维。
ax3.scatter3D(x, y, z, cmap='green')

A = points      # 样本矩阵
N = points.shape[0]

miu = A.mean(0)
miu = miu.reshape([1, 3])
center = miu        # 网格中心点


B = A-np.matmul(np.ones([N, 1]), miu)   # 均值点移动原点的样本矩阵
C = np.matmul(B.transpose(), B)/(N-1)

[lam, vector] = np.linalg.eig(C)
normal = np.array([vector[2][0], vector[2][1], vector[2][2]])
v_pca1 = np.array([vector[0][0], vector[0][1], vector[0][2]])
v_pca2 = np.array([vector[1][0], vector[1][1], vector[1][2]])


normal = normal/np.linalg.norm(normal, 2)
v_pca1 = v_pca1/np.linalg.norm(v_pca1, 2)
v_pca2 = v_pca2/np.linalg.norm(v_pca2, 2)

# 画图
print(type(center[0][0]))
l = np.linspace(-100, 100, 200)
xn = center[0][0]*np.ones([200, ])+normal[0]*l
yn = center[0][1]*np.ones([200, ])+normal[1]*l
zn = center[0][2]*np.ones([200, ])+normal[2]*l


x1 = center[0][0]*np.ones([200, ])+v_pca1[0]*l
y1 = center[0][1]*np.ones([200, ])+v_pca1[1]*l
z1 = center[0][2]*np.ones([200, ])+v_pca1[2]*l

x2 = center[0][0]*np.ones([200, ])+v_pca2[0]*l
y2 = center[0][1]*np.ones([200, ])+v_pca2[1]*l
z2 = center[0][2]*np.ones([200, ])+v_pca2[2]*l

# ax3.plot3D(xn, yn, zn, 'black')
# ax3.plot3D(x1, y1, z1, 'red')
# ax3.plot3D(x2, y2, z2, 'blue')






