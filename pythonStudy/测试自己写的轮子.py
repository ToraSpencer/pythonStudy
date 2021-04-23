import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
from mpl_toolkits import mplot3d
from selfDefined import *

toothTri = objReadTriangles('E:\\材料\\standardSphere.obj')



import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
mpl.rcParams['legend.fontsize'] = 20  # mpl模块载入的时候加载配置信息存储在rcParams变量中，rc_params_from_file()函数从文件加载配置信息
font = {
    'color': 'b',
    'style': 'oblique',
    'size': 20,
    'weight': 'bold'
}
fig = plt.figure(figsize=(16, 12))  #参数为图片大小
ax = fig.gca(projection='3d')  # get current axes，且坐标轴是3d的
#ax.set_aspect('equal')  # 坐标轴间比例一致
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection


# 四面体顶点和面
# verts = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 0, 1)]
# verts = np.asarray(verts)
# faces = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
# faces= np.asarray(faces)
# print(type(verts))
# print(type(faces))
# print(verts.shape)
# print(faces.shape)

verts = objReadVertices('E:\\材料\\standardSphere.obj')
verts = np.asarray(verts)
faces = objReadTriangles('E:\\材料\\standardSphere.obj')
faces = np.asarray(faces)
print(type(verts))
print(type(faces))
print(verts.shape)
print(faces.shape)



# 获得每个面的顶点
poly3d = [[verts[vert_id] for vert_id in face] for face in faces]

# 绘制顶点
x, y, z = zip(*verts)
ax.scatter(x, y, z)
# 绘制多边形面
ax.add_collection3d(Poly3DCollection(poly3d, facecolors='w', linewidths=1, alpha=0.3))
# 绘制多边形的边
ax.add_collection3d(Line3DCollection(poly3d, colors='k', linewidths=0.5, linestyles=':'))

# 设置图形坐标范围
ax.set_xlabel('X')
ax.set_xlim3d(-0.5, 1.5)
ax.set_ylabel('Y')
ax.set_ylim3d(-0.5, 1.5)
ax.set_zlabel('Z')
ax.set_zlim3d(-0.5, 1.5)
plt.show()