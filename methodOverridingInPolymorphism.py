class Animal:
    def intro(self):
        print("There are different types of animals.")
    
    def run(self):
        print("Most of the animals run faster.")

class Dog(Animal):
    def run(self):
        print("The dog ran him.")

class Cat(Animal):
    def run(self):
        print("The cat ran so fast as she moved up as she gets disappeared.")


a1 = Animal()
a1.intro()
a1.run()

d1 = Dog()
d1.intro()
d1.run()

c1 = Cat()
c1.intro()
c1.run()

