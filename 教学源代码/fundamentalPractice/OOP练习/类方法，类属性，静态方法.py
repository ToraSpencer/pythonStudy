#设计一个工具生成器，
class House(object):
    pass

class Tools(object):
    #类属性
    count = 0
    #静态方法，和类定义和实例化对象中的所有属性，方法都没有关系。
    @staticmethod
    def selfIntroduce():
        print('I am a tool box, i can generate tools')
    #类方法
    @classmethod
    def prt(cls):
        print('now you have %d tools' % Tools.count)
    def __init__(self,name):
        self.name = name
        print('You have a %s !' % self.name)
        Tools.count += 1
        pass

Tools.selfIntroduce()
axi = Tools('aix')
Tools.prt()


