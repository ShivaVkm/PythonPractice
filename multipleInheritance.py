class Animal(object):
    def __init__(self):
        self.name = "Horse"
        print("This is the animal class")
    

class Dog(object):
    def __init__(self):
        self.nameOfDog = "Juju"
        print("This is the dog class")

class Cat(Animal, Dog):
    def __init__(self):
        Animal.__init__(self)
        Dog.__init__(self)
        print("This is the cat class")

    def nameOfAnimals(self):
        print(self.name,"and "+ self.nameOfDog)


c1 =  Cat()
c1.nameOfAnimals()
        
