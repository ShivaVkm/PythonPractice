# def fibo(n):
#     a = 0
#     b = 1
#     while a < n:
#         print(a, end=" ")
#         a = b
#         b = a + b


# fibo(23)





# def make_incrementer(n):
#     return lambda x: x + n
# f = make_incrementer(45)
# print(f(56))





# def f(a, L = []):
#     L.append(a)
#     return L
# print(f(1))
# print(f(2))
# print(f(5))




# from pygame import mixer
# musicalFile = 'tumHiAana.mp3'
# mixer.init()
# mixer.music.load(musicalFile)
# mixer.music.play()



# from playsound import playsound
# playsound('tumHiAana.mp3')








# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
        
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')



# topProgrammingLanguages = ['Python','JavaScript','Java','Go','PHP','']
# class MyClass:
#     variable = "blah"

#     def function(self):
#         print("This is a message inside the class.")

# myobjectx = MyClass()
# myobjecty = MyClass()

# myobjecty.variable = "yackity"

# # Then print out both values
# print(myobjectx.variable)
# print(myobjecty.variable)









# sem5Subjects = ['Next Generation Technology', 'Advanced Web Programming', 'Artificial Intelligence']
# sem5Subjects.append('Software Project Management')
# print(sem5Subjects)
# sem5Subjects.append('Internet of Things')
# print(sem5Subjects)










# def hello():
#     print("Hello, Coders!")

# hello()







# def getInteger():
#     result = int(input("Enter the integer number:"))
#     return result

# def Main():
#     print("Main function started here guys!")
#     output = getInteger()
#     return output


# if __name__ =="__main__":
#     Main()











# # Python program to illustrate 
# # math module 
# import math 
  
# def Main(): 
#     num = float(input("Enter a number: ")) 
  
#     # fabs is used to get the absolute value of a decimal 
#     num = math.fabs(num)  
#     print(num) 
# if __name__=="__main__": 
#     Main()










# # Python code to demonstrate 
# # True, False, None, and, or , not 

# # showing that None is not equal to 0 
# # prints False as its false. 
# print (None == 0) 

# # showing objective of None 
# # two None value equated to None 
# # here x and y both are null 
# # hence true 
# x = None
# y = None
# print (x == y) 

# # showing logical operation 
# # or (returns True) 
# print (True or False) 

# # showing logical operation 
# # and (returns False) 
# print (False and True) 

# # showing logical operation 
# # not (returns False) 
# print (not True) 










# a = [25, 50, 100, 200, 300]
# del a[3]
# print(a)

# assert 50>100, '50 is not greater than 100'







# if 's' in 'geeksforgeeks':
#     print("s is part of gfg.")
# else:
#     print('s is not the part of gfg.')









# # Python code to demonstrate working of 
# # in and is 

# # using "in" to check 
# if 's' in 'geeksforgeeks': 
# 	print ("s is part of geeksforgeeks") 
# else : print ("s is not part of geeksforgeeks") 








# # using "in" to loop through 
# for i in 'geeksforgeeks': 
# 	print (i,end=" ") 

# print('\r')


	
# # using is to check object identity 
# # string is immutable( cannot be changed once alloted) 
# # hence occupy same memory location 
# print ('  ' is ' ') 

# # using is to check object identity 
# # dictionary is mutable( can be changed once alloted) 
# # hence occupy different memory location 
# print ({} is {}) 





# print("These are the\r this")











# # Python code to demonstrate working of 
# # global and non local 

# #initializing variable globally 
# a = 10

# # used to read the variable 
# def read(): 
# 	print (a) 

# # changing the value of globally defined variable 
# def mod1(): 
# 	global a 
# 	a = 5

# # changing value of only local variable 
# def mod2(): 
# 	a = 15

# # reading initial value of a 
# # prints 10 
# read() 

# # calling mod 1 function to modify value 
# # modifies value of global a to 5 
# mod1() 

# # reading modified value 
# # prints 5 
# read() 

# # calling mod 2 function to modify value 
# # modifies value of local a to 15, doesn't effect global value 
# mod2() 

# # reading modified value 
# # again prints 5 
# read() 

# # demonstrating non local 
# # inner loop changing the value of outer a 
# # prints 10 
# print ("Value of a using nonlocal is : ",end="") 
# def outer(): 
# 	a = 5
# 	def inner(): 
# 		nonlocal a 
# 		a = 10
# 	inner() 
# 	print (a) 

# outer() 

# # demonstrating without non local 
# # inner loop not changing the value of outer a 
# # prints 5 
# print ("Value of a without using nonlocal is : ",end="") 
# def outer(): 
# 	a = 5
# 	def inner(): 
# 		a = 10
# 	inner() 
# 	print (a) 

# outer() 











# class CodersTechnologies:

#     def pythonDeveloper():
#         print("He is the topnotch python developer!")

#     def javaScriptDeveloper():
#         print("He is the topnotch javaScript developer!")

#     def javaDeveloper():
#         print("He is the topnotch java developer!")


#  if __name__ == "__main__":
#      CodersTechnologies ct = CodersTechnologies()
#      ct.pythonDeveloper()
#      ct.javaScriptDeveloper()
#      ct.javaDeveloper()








# # var1 is in the global namespace  
# var1 = 5
# def some_func(): 
  
#     # var2 is in the local namespace  
#     var2 = 6
#     def some_inner_func(): 
  
#         # var3 is in the nested local  
#         # namespace 
#         var3 = 7











# # Python program processing 
# # global variable 

# count = 10
# def countDemo():
#     global count
#     count = count+1
#     print(count)
# countDemo()







# # Python program showing 
# # a scope of object 

# def some_func(): 
# 	print("Inside some_func") 
# 	def some_inner_func(): 
# 		var = 10
# 		print("Inside inner function, value of var:",var) 
# 	some_inner_func() 
# 	print("Try printing var from outer function: ",var) 
# some_func() 






# # Example 

# a = 10; b = 20; c = b + a;

# print(a); print(b); print(c) 










# # Bad Practice as width of this code is too much.
 
# #code
# x = 10
# y = 20
# z = 30
# no_of_teachers = x
# no_of_male_students = y
# no_of_female_students = z
 
# if (no_of_teachers == 10 and no_of_female_students == 30 and no_of_male_students == 20 and (x + y) == 30):
#     print('The course is valid')
 
# # This could be done instead:
 
# if (no_of_teachers == 10 and no_of_female_students == 30
#     and no_of_male_students == 20 and x + y == 30):
#     print('The course is valid')








# # Example 

# x =\
# 	1 + 2 \ 
# 	+ 5 + 6 \ 
# 	+ 10

# print(x) 







# #Instead of writing this massive Python code we can also code this in a different way 

# #Python code to demonstrate working of iskeyword() 

# # importing "keyword" for keyword operations 

# import keyword
# # initializing strings for testing while putting them in an array 
# keys = ["for", "while", "tanisha", "break", "sky", 
# "elif", "assert", "pulkit", "lambda", "else", "sakshar"] 

# for i in range(len(keys)): 
# 	# checking which are keywords 
# 	if keyword.iskeyword(keys[i]): 
# 		print(keys[i] + " is python keyword") 
# 	else: 
# 		print(keys[i] + " is not a python keyword") 








# #Python code to demonstrate working of iskeyword() 

# # importing "keyword" for keyword operations 
# import keyword 

# # printing all keywords at once using "kwlist()" 
# print ("The list of keywords is : ") 
# print (keyword.kwlist) 









# import keyword
# print("The list of python keywords are:")
# print(keyword.kwlist)





 

# # Python 3 code for printing 
# # on the same line printing 
# # geeks and geeksforgeeks 
# # in the same line 

# print("geeks", end =" ") 
# print("geeksforgeeks") 

# # array 
# a = [1, 2, 3, 4] 

# # printing a element in same 
# # line 
# for i in range(4): 
# 	print(a[i], end =" ") 








# i = 20
# if i == 20: print("The ",i," is equal to 20.")







# # Python program to illustrate short hand if-else 
# i = 10
# print(True) if i < 15 else print(False) 











# # Python program for simple calculator 

# # Function to add two numbers 
# def add(num1, num2): 
# 	return num1 + num2 

# # Function to subtract two numbers 
# def subtract(num1, num2): 
# 	return num1 - num2 

# # Function to multiply two numbers 
# def multiply(num1, num2): 
# 	return num1 * num2 

# # Function to divide two numbers 
# def divide(num1, num2): 
# 	return num1 / num2 

# print("Please select operation -\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n") 


# # Take input from the user 
# select = int(input("Select operations form 1, 2, 3, 4 :")) 

# number_1 = int(input("Enter first number: ")) 
# number_2 = int(input("Enter second number: ")) 

# if select == 1: 
# 	print(number_1, "+", number_2, "=", 
# 					add(number_1, number_2)) 

# elif select == 2: 
# 	print(number_1, "-", number_2, "=", 
# 					subtract(number_1, number_2)) 

# elif select == 3: 
# 	print(number_1, "*", number_2, "=", 
# 					multiply(number_1, number_2)) 

# elif select == 4: 
# 	print(number_1, "/", number_2, "=", 
# 					divide(number_1, number_2)) 
# else: 
# 	print("Invalid input") 








# # Python program showing how to
# # multiple input using split

# # taking two inputs at a time
# x, y = input("Enter a two value: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)
# print()

# # taking three inputs at a time
# x, y, z = input("Enter a three value: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)
# print()

# # taking two inputs at a time
# a, b = input("Enter a two value: ").split()
# print("First number is {} and second number is {}".format(a, b))
# print()

# # taking multiple inputs at a time 
# # and type casting using list() function
# x = list(map(int, input("Enter a multiple value: ").split()))
# print("List of students: ", x)










# listOfTopCoders = list(map(str, input("Enter the name of the top coders:").split(',')))
# print("The list of the top coders are ",listOfTopCoders)











# #code for disabling the softspace feature 
# print('G','F','G', sep='') 

# #for formatting a date 
# print('09','12','2016', sep='-') 

# #another example 
# print('pratik','geeksforgeeks', sep='@') 






# print('Coders','Geeks','Programmer','Developer','Engineer', sep='-')








# print('G','F', sep='', end='') 
# print('G') 
# #\n provides new line after printing the year 
# print('09','12', sep='-', end='\n') 

# print('prtk','agarwal', sep='', end='@') 
# print('geeksforgeeks') 






# myName = "Shiva Vishwakarma"
# number = 1
# # print("My name is %s and number is %s"%(myName,number))

# # print(f"My name is {myName} and numbr is {number}.")

# res = "name is {} and number is {}"
# finalResult = res.format(myName,number)
# print(finalResult)











# # Python program to illustrate 
# # *args for variable number of arguments
# def myFun(*argv): 
# 	for arg in argv: 
# 		print (arg)

# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 


# print()
# def nonKeywordedArgumentsDemo(* args):
#     for arg in args:
#         print(arg)

# nonKeywordedArgumentsDemo("pythonDeveloper","javaDeveloper","javaScriptDeveloper")







# stringDemo = "This is the string demo here."
# print(stringDemo)
# listDemo = [1, "ElonMusk","BillGates",1+2, "Steve Jobs"]
# print(listDemo)
# listDemo.append("RichestTechnologist")
# print(listDemo)
# listDemo.pop()
# print(listDemo)
# listDemo.append("MukeshAmbani")







# tupleDemo = ("GoogleMeet", 1, "GoogleDuo", 2, "GoToMeeting", 3, "Zoom")
# print(tupleDemo)
# aNumberDemo = 0
# while(aNumberDemo<=10):
#     print(aNumberDemo)
#     aNumberDemo = aNumberDemo+1







# greetingDemo = "Hello World! Welcome to the python programming world."
# for greetingIterations in greetingDemo:
#     print(greetingIterations,end="  ")








# for expectedResult in range(0,11):
#     print(expectedResult)

# codersGangList = ['Shiva Vishwakarma','Pratham Jaiswal','Madhav Jha','Vimal Maurya','Rakesh Yadav','Dinesh Padhi']
# for codersGangIterations in codersGangList:
#     print(codersGangIterations)







# stringDemo = "codeTodayToGetABetterTomorrow"
# print(stringDemo)
# print(stringDemo[0])
# print(stringDemo[-1])










# yourName = "Shiva Vishwakarma"
# del yourName 












# # Python Program for 
# # Formatting of Strings 

# # Default order 
# String1 = "{} {} {}".format('Geeks', 'For', 'Life') 
# print("Print String in default order: ") 
# print(String1) 

# # Positional Formatting 
# String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
# print("\nPrint String in Positional order: ") 
# print(String1) 

# # Keyword Formatting 
# String1 = "{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life') 
# print("\nPrint String in order of Keywords: ") 
# print(String1) 





















# s = 'geeksforgeeks'
# # Using for loop
# for letter in s:
  
#     print(letter)
#     # break the loop as soon it sees 'e'
#     # or 's'
#     if letter == 'e' or letter == 's':
#         break
  
# print("Out of for loop")
# print()






# print("shiva","geeksforgeeks", sep = "@")
# print("10","06","2001", sep = "/")
# print("Python is amazing to use for the development purpose")







# print("My name is Shiva", end = " ")
# print("Vishwakarma")





# a = 20
# b = 30
# res = a if a>b else b
# print(res)







# print("Geeks" * 5)







# print(all([False,False]))
# print(all([True,False,True]))
# print(all([True,True,True]))








# i = 1
# while(i<11):
#     print(i)
#     i += 1






# string1 = "shiva"
# print(max(string1))
# print(min(string1))
# string_in_uppercase = string1.upper()
# string_in_lowercase = string1.lower()
# print(string_in_uppercase)
# print(string_in_lowercase)




# create_a_tuple = tuple("Geeks")
# print(create_a_tuple)




# strings = "geeksforgeeks"
# res = set(strings)
# print(res)






# numbersOfSets = {1,1,1,1,1,1,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,5,5,5,5,5,5,5}
# print(set(numbersOfSets))









# nameOfStudent = "Shiva Vishwakarma"
# setResultOfNameOfStudent = set(nameOfStudent)
# print(setResultOfNameOfStudent)




# d = dict()
# d['abc'] = 1
# d['xyz'] = 2
# d['pqr'] = 3
# print(d)




# import keyword
# print(keyword.kwlist)




# import array
# arrayList = array.array('i',[1,2,3,4,5,6,7,8,9,10])
# for i in range(0,10):
#     print(arrayList[i], end = "     ")






# for key, value in enumerate(["The","Big","Bang","Theory"]):
#     print(key, value)






# # python code to demonstrate working of zip()

# # initializing list
# questions = ['name', 'colour', 'shape']
# answers = ['apple', 'red', 'a circle']

# # using zip() to combine two containers
# # and print values
# for question, answer in zip(questions, answers):
# 	print('What is your {0}? I am {1}.'.format(question, answer))






# def nonKeywordedArgs(*args):
# 	for arg in args:
# 		print(arg,end="	")

# nonKeywordedArgs("hello","coders","geeks")




# def keyWordedArgs(**kwargs):
# 	for key, value in kwargs.items():
# 		print("%s==%s"%(key,value), end = "	")

# keyWordedArgs(firstName = "Shiva", lastName = "Vishwakarma")





# def myFunction(arg1, arg2, arg3):
# 	print("arg1", arg1)
# 	print("arg2", arg2)
# 	print("arg3", arg3)

# args = ("geeks","for","geeks")
# myFunction(*args)


# kwargs = {"arg1":"Shiva", "arg2":"Vishwakarma","arg3":"coder"}
# myFunction(**kwargs)





# def yieldDemo():
# 	yield 1
# 	yield 2
# 	yield 3

# for value in yieldDemo():
# 	print(value)





# print(100+1000+2000+100000+200000)










# def nextSqaure():
# 	i = 1
# 	while(True):
# 		yield i*i
# 		i = i+1

# for number in nextSqaure():
# 	if(number>100):
# 		break
# 	print(number)








# cubeOfGivenNumber = lambda x: x*x*x
# print(cubeOfGivenNumber(5))





# # Returning functions from another functions.
# def mathematicalOperation(num1):
#     def addition(num2):
#         return num1 + num2
#     return addition

# res = mathematicalOperation(20)
# print(res(10))





