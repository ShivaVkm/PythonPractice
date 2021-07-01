class GrandFather:
    def __init__(self, grandFatherName):
        self.grandFatherName = grandFatherName

class Father(GrandFather):
    def __init__(self, fatherName, grandFatherName):
        self.fatherName = fatherName

        GrandFather.__init__(self, grandFatherName)   # instead of GrandFather we can also super() keyword


class Son(Father):
    def __init__(self, sonName, fatherName, grandFatherName):
        self.sonName = sonName

        Father.__init__(self, fatherName, grandFatherName)


    def showNames(self):
        print("Grand Father's name: ",self.grandFatherName)
        print("Father's name: ",self.fatherName)
        print("Son's name: ",self.sonName)



s1 = Son("Shiva", "Lalu", "Badri")
print(s1.grandFatherName)
s1.showNames()

