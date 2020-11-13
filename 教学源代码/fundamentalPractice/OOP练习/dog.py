#继承
class animal:
    def eat(self):
        print('all animals need to eat')
        pass
class dog(animal):
    def eat(self):
        super().eat()
        print('dogs love to eat meat.')
        pass

xiaomin = dog()
xiaomin.eat()
print(dir())