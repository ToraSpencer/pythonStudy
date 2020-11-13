import random
import math
import time
N = 1000000;
hits = 0;
time.clock()
for i in range(1,N):
    x,y = random.random(),random.random()
    r = math.sqrt(x**2+y**2)
    if r<=1.0:
        hits = hits+1
pi = 4*(hits/N)
print('实验求得的pi值为：',pi,'\n')
print('程序运行时间为：%-5.5ss'%time.clock())

