class Employee:
    def __init__(self):
        print("Employee constructor is created.")
    def __del__(self):
        print("Destructor is called and Employee constructor is deleted.")

e1 = Employee()
del e1