class Father:
    fatherName = ""
    def father(self):
        print(self.fatherName)

class Mother:
    motherName = ""
    def mother(self):
        print(self.motherName)

class Son(Father, Mother):
    def parent(self):
        print("Father's name: ",self.fatherName)
        print("Mother's name: ",self.motherName)


s1 = Son()
s1.fatherName = "Raam"
s1.motherName = "Seetaa"
s1.parent()