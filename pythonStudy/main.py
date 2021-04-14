# python中的宏函数
def print_hi(name):
    print(f'Hi, {name}')             # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')




# numpy, matplotlib
import matplotlib.pyplot as plt  # matplotlib是一个第三方绘图类；pyplot是一个接口类，提供了matlab风格的一些绘图接口。
plt.style.use('seaborn-whitegrid')
import numpy as np
from mpl_toolkits import mplot3d  # 导入mplot3d工具包，激活三维绘图功能。



'''读取OBJ文件数据'''
import os


# # 局部坐标系下的颌数据
# objFilePath = 'E:\\jawOut.obj'
# with open(objFilePath) as file:
#     points = []
#     while 1:
#         line = file.readline()
#         if not line:
#             break
#         strs = line.split(" ")
#         if strs[0] == "v":
#             points.append((float(strs[1]), float(strs[2]), float(strs[3])))
#         if strs[0] == "vt":
#             break


# from selfDefined import readOBJ
# path = 'E:\\jawOut.obj'
# points = readOBJ(path)
# print(points)
# import sys
# print(sys.getsizeof(points))
#
#
# from selfDefined import foo
# foo()









