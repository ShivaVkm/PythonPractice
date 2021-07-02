# try:
#     num1 = 10
#     num2 = 15
#     if(num1 < num2):
#         div1 = num1 > num2  #ZeroDivisionError
#     print(div1)             #NameError

# except(ZeroDivisionError, NameError):
#     print("Error occured and handled here")






print()
print("Another example")
print()

def DivisionOfMultipleNumbers(num1, num2):
    try:
        div = ((num1+num2) / (num1-num2))
    except ZeroDivisionError:
        print("This resulted in zero ('0')")
    else:
        print("The result of the division of numbers are ",div)


DivisionOfMultipleNumbers(2, 2)
DivisionOfMultipleNumbers(9, 10)