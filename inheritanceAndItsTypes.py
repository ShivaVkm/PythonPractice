# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def getName(self):
#         return self.name
    
#     def isEmployee(self):
#         return False

# class Employee(Person):
#     def isEmployee(self):
#         return True


# e1 = Employee("Shiva")
# print(e1.getName(),e1.isEmployee())

# e1 = Person("Pratham")
# print(e1.getName(), e1.isEmployee())




class A:
    def __init__(self):
        print("in A init")
    
    def feature(self):
        print("Feature of class A")
    
class B:
    def __init__(self):
        print("in B init")
    
    def feature(self):
        print("Feature of class B")

class C(A,B): # Method Resolution Order (MRO)
    def __init__(self):
        super().__init__() # it also selects as left one constructors so we can say it follows
                            # Constructor Resolution Order
        print("in C init")



c1 = C()
c1.feature()   # Method Resolution Order (MRO) where it will call the method of the left side 
                # class passed inside the parenthesis of class C
