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


''' 函数————读取纯点集OBJ文件'''
def readOBJ(filePath):
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
            if strs[0] == "vt":
                break
        return points



def foo():
    print("hahahah")
    return
