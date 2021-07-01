class Animal:
    color = "white"
    def speak(self):
        print("Animal is speaking")


class Dog(Animal):
    # color = "Brown"
    def bark(self):
        print("The dog is barking")
    

d1 = Dog()
d1.speak()
print(d1.color)
d1.bark()