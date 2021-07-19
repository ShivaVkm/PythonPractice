# class Dog:
#     color = 'white'

#     def bark(self):
#         print("The dog is barking")

# Rodger = Dog()
# print(Rodger.color)
# Rodger.bark()
    




# # Parameterized constructor
# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def displayDetails(self):
#         print("The name of the person is",self.name+".")

# p = Person("Shiva")
# p.displayDetails()




## Another example of the parameterized constructor
# class Addition:
#     firstNumber = 0
#     secondNumber = 0
#     answer = 0

#     def __init__(self, f, s):
#         self.firstNumber = f
#         self.secondNumber = s


#     def calculate(self):
#         self.answer = self.firstNumber + self.secondNumber


#     def display(self):
#         print("First number is "+str(self.firstNumber))
#         print("Second number is "+str(self.secondNumber))
#         print("Answer is "+str(self.answer))
    

# a1 = Addition(1000, 2000)
# a1.calculate()
# a1.display()




# number = int(input("Enter a number"))
# while number>0:
#     remainder = number % 10
#     reversedNumber = 0
#     reversedNumber = reversedNumber * 10 + remainder
#     number = number // 10
# if(number == reversedNumber):
#     print("Its palindrome number")
# else:
#     print("Its not the palindrome number")








class A:
    def feature1(self):
        print("Hello class A feature")

class B:
    def feature2(self):
        print("Hello class B feature")

class C(A,B):
    def feature3(self):
        print("Hello class C feature")


c = C()
c.feature3()
c.feature2()
c.feature1()
