#需求：小民体重75公斤，每次跑步减肥0.5公斤，每次吃东西增肥1公斤。
class Person:
#在本算法中关心对象的两个属性：名字，体重。
     def __init__(self,name,weight):
        self.name = name
        self.weight = weight
     def __str__(self):
         return 'my name is %s,my weight is %.2f kg'%(self.name,self.weight)
     def run(self):
         print('%s is running' % self.name)
         self.weight = self.weight-0.5
         pass
     def eat(self):
         print('%s is eating' % self.name)
         self.weight = self.weight+1
         pass
     def selfIntroduce(self):
         print('my name is %s,now my weight is %.2fkg' % (self.name,self.weight))
         pass
xiaomin = Person('xiaomin',98)
xiaomei = Person('xiaomei',70)

xiaomin.selfIntroduce()
xiaomin.eat()
xiaomin.run()
xiaomin.selfIntroduce()
xiaomei.selfIntroduce()
xiaomei.run()
xiaomei.eat()
xiaomei.eat()
xiaomei.selfIntroduce()



