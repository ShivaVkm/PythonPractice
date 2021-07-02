# decoraters are functions which are used to add functionalities to the existing 
# functions without permanently modyfying the existing function.

def Division(number1, number2):
    print(number1/number2)

def DecoratedDivision(function):
    
    def InnerDecoratedDivision(n1, n2):
        if n1<n2:
            n1, n2 = n2, n1
        return function(n1, n2)
    return InnerDecoratedDivision


result = DecoratedDivision(Division)
result(2,9)





print("####################Another Example#######################")
print()



def greetToWorld():
    print("Hello everybody in this world", end = " ")

def greetToIndia(functionGreetObj):
    def greetToMaharashtra():
        functionGreetObj()
        print("of Maharashtra!")
        print("Greeted well!")
    return greetToMaharashtra

greetedObject = greetToIndia(greetToWorld)
greetedObject()





print("######################## OR This Way ##############################")






def greetToIndia(functionGreetObj):
    def greetToMaharashtra():
        functionGreetObj()
        print("of Maharashtra!")
        print("Greeted well!")
    return greetToMaharashtra

@greetToIndia
def greetToWorld():
    print("Hello everybody in this world", end = " ")

greetToWorld()