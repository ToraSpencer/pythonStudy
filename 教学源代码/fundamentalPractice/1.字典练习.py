#练习创建字典，以及对字典元素的操作。
#创建一个alien字典，代表一个外星人对象，内容为外星人的基本信息：颜色，分数(玩家射杀后得分)
alien_0 = {'color':'green','points':5}

#获取字典中某个键的值：
points = alien_0['points']
print('alion_0 is carried with ',points,' points','\n')

#给字典中增加新的键值对：给外星人增加位置坐标信息：
alien_0['x_position'] = 1
alien_0['y_position'] = 2
print('alien_0\'s location is (',alien_0['x_position'],',',alien_0['y_position'],')\n')

#修改字典中某个键对应的值：直接赋值
alien_0['x_position'] = 3
print('alien_0\'s location is (',alien_0['x_position'],',',alien_0['y_position'],')\n')

#删除键值对
del alien_0['color']
print(alien_0)
alien_0['color'] = 'green'

#