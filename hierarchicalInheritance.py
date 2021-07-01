# when different child/sub/base classes inherit the properties and behaviors of the 
# parent/super/derived class then it is called as Hierarchical Inheritance

class Parent:
    def parent(self):
        print("This is the Parent class's method.")

class Child1(Parent):
    def child1(self):
        print("This is the Child1 class's method.")

class Child2(Parent):
    def child2(self):
        print("This is the Child2 class's method.")

# Object creation and its execution
c1 = Child1()
c2 = Child2()
c1.child1()
c1.parent()
c2.child2()
c2.parent()