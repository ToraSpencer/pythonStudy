from FurnitureAndHouse import *
table = Furniture('table',2)
chair = Furniture('chair',1)
closet = Furniture('closet',3)
bed = Furniture('bed',5)
my_house = House('villa',1000)

my_house.addFurniture(table)
my_house.addFurniture(chair)
my_house.addFurniture(closet)
my_house.addFurniture(bed)
print(my_house)

from SoldierWithAGun import *

AK48 = Gun('AK48',10)
XiaoMin = Soldier('XiaoMin',AK48)

print(XiaoMin)
XiaoMin.shoot()
print(XiaoMin)
XiaoMin.add_bullet()
print(XiaoMin)

help(None)