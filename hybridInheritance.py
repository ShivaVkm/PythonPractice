# An inheritance which consists of multiple types of inheritance is called Hybrid Inheritance

class College:
    def college(self):
        print("This college mainly focuses on programming and technology.")

class Student1(College):     # Single Inheritance is getting performed
    def student1(self):
        print("First student Rohan writes the clean code.")


class Student2(College):   # Student1 and Student2 classes are Hierarchical Inheritance
    def student2(self):
        print("Second student develops the awesome and useful real world projects.")
        

class Student3(Student1, College):    # multiple inheritance
    def student3(self):
        print("Third student tests the projects thoughroughly.")



# Here the code drives completely the above codes
s3 = Student3()
s3.college()
s3.student1()
s3.student3()
s3.student2() # this gives an error as "AttributeError: 'Student3' object has no attribute 'student2'"