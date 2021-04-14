# 在pycharm中使用第三方库，设置 → Python interpreter 中搜索第三方库，然后install
import matplotlib.pyplot as plt             # matplotlib是一个第三方绘图类；pyplot是一个接口类，提供了matlab风格的一些绘图接口。
plt.style.use('seaborn-whitegrid')
import numpy as np
from mpl_toolkits import mplot3d            # 导入mplot3d工具包，激活三维绘图功能。

''' numpy介绍'''
"""
    numpy(numerical python)是一个开源的科学计算库，可以取代Matlab和Mathematica的部分功能，
    最初的NumPy其实是SciPy的一部分，后来才从SciPy中分离出来。如今，SciPy在处理数组和矩阵时会调用NumPy。
    numpy支持C语言API
    
"""





''' numpy数组'''
"""
    numpy数组在数值计算方面的效率优于python自己的list容器，但是通用性则差于list
    
"""


# '''生成矩阵、向量的常用接口'''
# x = np.arange(0, 10, 0.1)           # numpy.arange(start, stop, stepLen, dtype = None)，注意区间是前闭后开的。
# x = np.linspace(0.001, 10, 1000)    # numpy::linspace(起点：终点：步数)
# a = np.ones([3,4])                  # 全1矩阵
# '''     np.asarray()——输入tuple, list对象，输出矩阵'''
# list1 = [1, 2, 3]
# tuple1 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# list2 = [(-1, -2, -3), (-4, -5, -6)]
# array1 = np.asarray(list1)
# array2 = np.asarray(tuple1)
# array3 = np.asarray(list2)



# ''' 获取矩阵的元素、性质'''
# a.shape                       # 矩阵行列数
# print(a[0])                   # 矩阵第一行
# print(a[0][0])                # 矩阵第一个元素
# row = a.shape[0]              # 行数
# col = a.shape[1]              # 列数



''' 基本矩阵变换、运算'''
# a = [1,1,1]
# b = [2,2,2]
# print(np.prod(b))          # 矩阵、向量的元素连乘乘积
# c = np.vstack([a,b])
# print(np.sum(c,1))          # 0表示对列求和，压成一行；1表示对行求和，压成一列，然后转置成一行输出。
# print(np.sum(c,0))
# print(c.sum(1))             # 矩阵对象自己的sum()方法和np的sum()方法类似
# print(c.sum(0))
# print(c.mean(1))            # 求平均mean()和sum()类似
# print(np.transpose(c))        # 矩阵转置
# print(a)
# print(np.transpose(a))        # transpose()函数对只有一行的矩阵没用，只能用reshape()实现
# print(a.reshape([3,1]))


'''     矩阵拼接'''
# m = np.vstack([a, b])       # 纵向拼接
# n = np.hstack([a, b])       # 横向拼接


'''     矩阵拆分'''
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print('\na ==\n', a)
[a1, a2] = np.vsplit(a, 2)       # 纵切
[b1, b2, b3] = np.hsplit(a, 3)    # 横切
print('\na1 ==\n', a1)
print('\nb1 ==\n', b1)


'''     矩阵运算'''
# print(np.matmul(b,c))          # 矩阵乘法用np.matmul()，按理说直接用*来乘是可以的，不知道为什么报错，可能是版本问题。
# print(np.multiply(a,a))        # 矩阵按元素相乘np.multiply()
# print(np.kron(a,b))            # 克罗内克积np.kron()


'''     高级矩阵变换、运算'''
# a = [1,2,3]
# b = [4, 5, 6]
# c = np.vstack([a,b])



'''         矩阵复制扩张np.tile()'''
# d = np.tile(c,[3,2])
# print(d)


'''         求特征值、特征向量np.linalg.eig()'''
# [lam, vector] = np.linalg.eig(a)    # 求矩阵的特征值、特征向量。
# print(lam)
# print(vector)

# aa = a.tolist()
# bb = b.tolist()
# print(aa.index(max(aa)))                # 找出向量中的最大值，及其在向量中的索引。
# print(bb.index(max(bb)))

# print(np.linalg.norm(a,1))        # 矩阵的一范数，即所有元素绝对值加和
# print(np.linalg.norm(a,2))        # 矩阵的二范数，如果矩阵是向量的话，就是其模长。


'''         求解线性方程组'''
# A = [[1, 2], [3, 4]]
# b = [1,2]
# A = np.array(A)
# b = np.array(b)
# b = b.reshape([2, 1])
# AA = np.linalg.inv(A)
# x = np.matmul(np.linalg.inv(A), b)
# print(x)


''' 线性代数计算工具numpy.linalg'''
"""
    numpy.linalg.inv(a)
                计算逆矩阵。
    
    numpy.linalg.pinv(a ,rcond)
                计算矩阵的（Moore-Penrose）伪逆。
    
    numpy.linalg.tensorinv(a ,ind)
                计算 N 维数组的逆。
                
    numpy.linalg.det(a)
                计算数组的行列式。
    
    numpy.linalg.slogdet(a)
                计算数组的行列式的符号和自然对数。
    
    numpy.trace(a ,offset,axis1,axis2,dtype,out)
                计算trace
    
    numpy.linalg.solve(a, b)
                求解线性矩阵方程或线性标量方程组。
                
    numpy.linalg.cholesky(a)
                Cholesky 分解。
                
    numpy.linalg.qr(a ,mode)
                计算矩阵的 QR 因式分解。
    
    numpy.linalg.svd(a ,full_matrices,compute_uv)
                奇异值分解。
    
    numpy.linalg.matrix_rank(M ,tol)
                使用奇异值分解方法返回秩。
    
    numpy.linalg.eig(a)
                计算正方形数组的特征值和右特征向量。
    
    numpy.linalg.eigvals(a)
                计算矩阵的特征值。
    
    numpy.linalg.eigh(a, UPLO)
                返回 Hermitian 或对称矩阵的特征值和特征向量。
    

    numpy.linalg.eigvalsh(a, UPLO)
                计算 Hermitian 或真实对称矩阵的特征值。
                
    numpy.linalg.norm(x ,ord,axis,keepdims)
                计算矩阵或向量范数。
    
    numpy.linalg.cond(x ,p)
                计算矩阵的条件数。
    
    numpy.linalg.tensorsolve(a, b ,axes)
                为 x 解出张量方程 a x = b
    
    numpy.linalg.lstsq(a, b ,rcond)
                将最小二乘解返回到线性矩阵方程。
    

"""




