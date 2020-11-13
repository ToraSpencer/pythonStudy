#需求：士兵某某有一把某某枪，枪有一定数量的子弹，士兵可以开枪。
class Soldier:
    def __init__(self,name,Gun):
        self.name = name
        self.Gun = Gun
        pass
    def __str__(self):
        return 'I\'m %s the soldier,my gun has %d bullets left' % (self.name,self.Gun.bullet)
    def shoot(self):
        self.Gun.bullet -= 1
        print('%s is shooting.' % self.name)
        pass
    def add_bullet(self):
        self.Gun.bullet += 1
        print('%s has added bullet' % self.name)
        pass


class Gun:
    def __init__(self,name,bullet):
        self.name = name
        self.bullet = bullet
    def __str__(self):
        print('This is a %s' % self.name)
        pass


