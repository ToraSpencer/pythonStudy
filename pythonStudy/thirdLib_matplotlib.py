

# numpy, matplotlib
# 在pycharm中使用第三方库，设置 → Python interpreter 中搜索第三方库，然后install
import matplotlib.pyplot as plt         # matplotlib是一个第三方绘图类；pyplot是一个接口类，提供了matlab风格的一些绘图接口。
plt.style.use('seaborn-whitegrid')
import numpy as np
from mpl_toolkits import mplot3d            # 导入mplot3d工具包，激活三维绘图功能。


''' 画图基本'''
"""
fig1 = plt.figure()          # pyplot::figure()方法——创建图形——可以包含维度、图像、文本、标签等等对象的容器。
ax1 = plt.axes()             # pyplot::axes()方法——创建维度。
x = np.linspace(0.001, 10, 1000)      # pyplot::linspace(起点：终点：步数)
plt.plot(x, np.sin(x))       # pyplot::plot()方法——画图线
plt.plot(x, np.cos(x))       # plot()方法可以多次调用画多条图线。
plt.plot(x, np.sin(x - 1), color='blue')    # plot()中指定颜色
plt.plot(x, x + 2, '-.k')                   # plot()中使用字符串指定图线风格：黑色长短点虚线

# plot中指定标签，然后调用pyplot::legend()方法,可以生成图例来指示图线。
plt.plot(x, np.log(x), label='y = log(x)')
plt.legend()

# 各种名字——不支持中文
plt.title("this is a title")
plt.xlabel("x")
plt.ylabel("y")

plt.show()              # pyplot::show()方法——显示图形




# 创建第二幅图形
fig2 = plt.figure()
ax1 = plt.axes()
x = np.linspace(0, 10, 50)

"""


''' 画散点图'''
"""
plt.plot(x, np.sin(x), 'o', color='red')
plt.plot(x, np.cos(x), '-ok')               # 点线，黑色
plt.plot(x, np.sin(x+1), '+', color='blue')

plt.show()
"""


''' 画直线'''
"""
    已知y = f(x)函数关系：
        x = np.linspace(0.001, 10, 1000)       
        y = np.sin(x)
        plt.plot(x, y)        
    
    
    已知直线方向向量：
        vec = [44.3305, -3.83421]
        x1 = np.linspace(-30, 30, 200)
        y1 = x1*vec[1]/vec_x[0]
    

"""


''' 画曲线'''
"""
    使用contour()直接输入标准方程画图线。
        x0 = np.linspace(-10, 10, 100)
        y0 = x0
        x,y = np.meshgrid(x0,y0)
        z= x**2+y**2+x*y
        z=z.reshape(x.shape)            #z数组的大小必须和xx,yy大小一致
        plt.contour(x, y, z, [0, 9])        # 最后的数组参数中至少要有两个元素

"""


''' 画三维图'''
"""
    fig3 = plt.figure()
    ax3 = plt.axes(projection='3d')          # 关键字参数projection='3d'指定创建维度为三维。
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax3.scatter3D(xline, yline, zline, cmap='Blues')  #scatter3D()——画三维散点图。
    ax3.plot3D(xline, yline, zline, 'gray')     # pyplot::plot3D()方法——画三维图线
    plt.show()
"""




