class Animal:
    def __init__(self):
        print("Animal constructor is created.")
    
    def __del__(self):
        print("Animal Destructor is called.")

def cat():
    print("Making cat object")
    a1 = Animal()
    print("Function ends here")
    return a1

print("Calling the Cat function")
a1 = cat()
print("Program ends here")

