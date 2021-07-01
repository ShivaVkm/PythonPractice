# The private members of the parent class cannot be inherited into the child class.

class A:
    def __init__(self):
        self.n1 = 25
        self.__n2 = 45 # this is the private variable of the A class

class B(A):
    def __init__(self):
        self.n3 = 20
        A.__init__(self) 


b1 = B()
print(b1.n1," ",b1.n3)
print(b1.n2)  # this will return an error because n2 is a private member of the A class