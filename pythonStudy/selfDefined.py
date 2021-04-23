from typing import TextIO

import matplotlib.pyplot as plt  # matplotlib是一个第三方绘图类；pyplot是一个接口类，提供了matlab风格的一些绘图接口。
plt.style.use('seaborn-whitegrid')
import numpy as np
from mpl_toolkits import mplot3d  # 导入mplot3d工具包，激活三维绘图功能。
import os
import struct


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


''' 函数————读取OBJ文件中的顶点信息'''
def objReadVertices(filePath):
    file: TextIO
    with open(filePath) as file:
        points = []
        while 1:
            line = file.readline()
            if not line:
                break
            strs = line.split(" ")
            if strs[0] == "v":
                points.append((float(strs[1]), float(strs[2]), float(strs[3])))
            else:
                continue
        return points


def objReadTriangles(filePath):
    file: TextIO
    with open(filePath) as file:
        tris = []
        while 1:
            line = file.readline()
            if not line:
                break
            strs = line.split(" ")
            if strs[0] == "f":
                tris.append((int(strs[1]), int(strs[2]), int(strs[3])))
            else:
                continue
    return tris


''' 将点云画出来'''
def printVers(vers):
    vers_array = np.asarray(vers)
    [x, y, z] = np.hsplit(vers_array, 3)
    fig = plt.figure()
    ax3 = plt.axes(projection='3d')          # 关键字参数projection='3d'指定创建维度为三维。
    ax3.scatter3D(x, y, z, cmap='Blues')     # scatter3D()——画三维散点图。
    plt.show()



def foo():
    print("hahahah")
    return
