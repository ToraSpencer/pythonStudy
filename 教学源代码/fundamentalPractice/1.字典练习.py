#��ϰ�����ֵ䣬�Լ����ֵ�Ԫ�صĲ�����
#����һ��alien�ֵ䣬����һ�������˶�������Ϊ�����˵Ļ�����Ϣ����ɫ������(�����ɱ��÷�)
alien_0 = {'color':'green','points':5}

#��ȡ�ֵ���ĳ������ֵ��
points = alien_0['points']
print('alion_0 is carried with ',points,' points','\n')

#���ֵ��������µļ�ֵ�ԣ�������������λ��������Ϣ��
alien_0['x_position'] = 1
alien_0['y_position'] = 2
print('alien_0\'s location is (',alien_0['x_position'],',',alien_0['y_position'],')\n')

#�޸��ֵ���ĳ������Ӧ��ֵ��ֱ�Ӹ�ֵ
alien_0['x_position'] = 3
print('alien_0\'s location is (',alien_0['x_position'],',',alien_0['y_position'],')\n')

#ɾ����ֵ��
del alien_0['color']
print(alien_0)
alien_0['color'] = 'green'

#