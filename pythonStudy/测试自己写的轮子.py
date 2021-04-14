import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
from mpl_toolkits import mplot3d
from selfDefined import *

toothVer = objReadVertices('E:\\材料\\tooth.obj')
print(toothVer)
print(type(toothVer))

toothArray = np.asarray(toothVer)
print(toothArray)

[x, y, z] = np.hsplit(toothArray, 3)

print(x)
fig3 = plt.figure()
ax3 = plt.axes(projection='3d')          # 关键字参数projection='3d'指定创建维度为三维。
ax3.scatter3D(x, y, z, cmap='Blues')  #scatter3D()——画三维散点图。
plt.show()