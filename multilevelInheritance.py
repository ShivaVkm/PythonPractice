class GrandParent(object):
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name

class Parent(GrandParent):
    def __init__(self, name, age):
        GrandParent.__init__(self, name)
        self.age = age
    
    def getAge(self):
        return self.age

class Child(Parent):
    def __init__(self, name, age, address):
        Parent.__init__(self, name, age)
        self.address = address
    
    def getAddress(self):
        return self.address
        

c1 = Child("Shiva", 20, "Thane")
print(c1.getName(), c1.getAge(), c1.getAddress())