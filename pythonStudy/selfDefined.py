import matplotlib.pyplot as plt  # matplotlib是一个第三方绘图类；pyplot是一个接口类，提供了matlab风格的一些绘图接口。
plt.style.use('seaborn-whitegrid')
import numpy as np
from mpl_toolkits import mplot3d  # 导入mplot3d工具包，激活三维绘图功能。
import os
import struct



''' 自定义类————四元数类'''
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
        result = v + a + b
        return result

    def fromRotateAxis(self, vo, vd):
        return


''' 函数————读取文件中的double数组'''
def readDoubleArray(str):
    x = []
    with open(str, 'rb') as file:
        size = os.path.getsize(str)
        size = int(size / 8)
        for i in range(size):
            temp = file.read(8)
            temp = struct.unpack('d', temp)
            x.append(temp[0])
        file.close()
    return x


''' 函数————读取纯点集OBJ文件'''
def readOBJ(filePath):
    with open(filePath) as file:
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
        return points



def foo():
    print("hahahah")
    return
