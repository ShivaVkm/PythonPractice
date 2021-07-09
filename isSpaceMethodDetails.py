# isspace() method is used to check space space in the string

name = ""
res1 = name.isspace()
print(res1)



name = " "
res2 = name.isspace()
print(res2)



whiteSpaceCharacters = "\n\t\r\v\f"  # This contains whitespace characters so it will return True
name = "Shiva Vishwakarma"   # This contains a space with string so it will return False
res3 = whiteSpaceCharacters.isspace()
print(res3)
res4 = name.isspace()
print(res4)