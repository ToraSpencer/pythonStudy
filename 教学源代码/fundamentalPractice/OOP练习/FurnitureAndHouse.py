#需求：房子中添加家具。房子有户型，总面积，家具名称列表。
#家具有名字和占地面积。家具可以被添加到房子之中
#输出房子时，要输出户型，总面积，剩余面积，家具名称列表。
#要能够计算添加家具后房子剩余的面积
class Furniture:
    def __init__(self,name,area):
        self.name = name
        self.area = area
        pass
    def __str__(self):
        return '%s ocupies %f m^2 area' % (self.name,self.area)

class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.furniture_list = []
        pass
    def __str__(self):
        return 'the house\'s type is %s,with %f m^2 total area,and %f m^2 free area,' \
               'and has furnitures such as %s' % (self.house_type,self.area,self.free_area,self.furniture_list)
    def addFurniture(self,Furniture):
        self.free_area -= Furniture.area
        self.furniture_list.append(Furniture.name)
        print('the %s is added into the house.' % Furniture.name)
        pass



