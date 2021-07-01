class Base:
    def __init__(self):
        self._a = 20  # _ is used to create the protected member of a class

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling the protected members of the base class.")
        print(self._a)

d1 = Derived()
b1 = Base()
print(b1.a)  # AttributeError: 'Base' object has no attribute 'a' because a is the protected member of the Base class so it cannot be accessed outside the class

