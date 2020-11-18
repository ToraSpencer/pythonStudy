
# 注释

"""
    多行注释
"""
''' 单行注释'''
# 单行注释


''' 导入模块、函数'''
"""
    import timeit           # 导入整个模块
    print(timeit.Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
    import numpy as np      # 导入整个模块并设置别名
    from math import pi     # 从模块中导入单个数据、函数，则使用的时候不需要模块名前缀
    from math import *      # 想要导入整个模块又懒得用别名就这样。
    print(pi)
"""

''' 基本语句'''
"""
    if-else条件分支 
        age = int(input("请输入你家狗狗的年龄: "))
        print("")
        if age <= 0:
            print("你是在逗我吧!")
        elif age == 1:
            print("相当于 14 岁的人。")
        elif age == 2:
            print("相当于 22 岁的人。")
        elif age > 2:
            human = 22 + (age - 2) * 5
            print("对应人类年龄: ", human)
        else:
            print("错误")



    while循环 
        n = 100
        sum = 0
        counter = 1
        while counter <= n:
            sum = sum + counter
            counter += 1
        print("1 到 %d 之和为: %d" % (n, sum))


    for循环 
        sites = ["Baidu", "Google", "Runoob", "Taobao"]
        for site in sites:
            if site == "Runoob":
                print("菜鸟教程!")
                break
            print("循环数据 " + site)
        else:
            print("没有循环数据!")
        print("完成循环!")


    for循环中使用range()函数 
        for i in range(5, 9):
            print(i)

        for i in range(-10, -100, -30):
            print(i)
"""

''' python中的逻辑运算符是and, or, not'''
