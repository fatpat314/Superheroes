class Animal:
    def __init__(self, name, eat, drink):
        self.name = name
        self.eat = eat
        self.drink = drink

    def eat(self):
        print("{} is eating".format(self.name))

    def drink(self):
        print("{} is drinking".format(self.drink))
