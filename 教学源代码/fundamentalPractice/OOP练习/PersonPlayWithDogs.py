#多态：不同的子类调用相同的方法，产生不同的结果。
class Dog(object):
    def __init__(self,name):
        self.name = name
        pass
    def play(self):
        print('%s is hopping.' % self.name)
        pass
class XiaoTianDog(Dog):
    def play(self):
        print('%s is flying' % self.name)
        pass
class Person(object):
    def __init__(self,name):
        self.name = name
    def playWithDog(self,Dog):
        Dog.play()
        pass


wangcai = Dog('wangcai')
beibei = XiaoTianDog('beibei')
xiaomin = Person('xiaomin')
xiaohong = Person('xiaohong')
xiaomin.playWithDog(wangcai)
xiaohong.playWithDog(beibei)
