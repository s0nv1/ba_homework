class Animal:
    def talk(self):
        pass

    def golos(self):
        self.talk()
        
        
class Dog(Animal):
    def talk(self):
        print('woof woof')


class Cat(Animal):
    def talk(self):
        print('meow meow')

d = Dog()
c = Cat()
c.golos()
d.golos()
