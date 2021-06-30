class A:
    def __init__(self, aa):
        self.a = aa

class B:
    def __init__(self):
        self.b = A(self)
    def __del__(self):
        print("Destructor gets called here.")

def objectCreation():
    b = B()

objectCreation()