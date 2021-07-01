class ITStudent:
    stream = "BTech-IT"
    def __init__(self, name, rollNo):
        self.name = name 
        self.rollNo = rollNo
    
its1 = ITStudent("Shiva", 28)
its2 = ITStudent("Raman", 27)

print(its1.stream)
print(its2.stream)
print(its1.name)
print(its2.name)     
print(its1.rollNo)
print(its2.rollNo)      

print(ITStudent.stream)
  

its1.stream = 'BSc-IT'
print(its1.stream)
print(its2.stream) 
  
ITStudent.stream = 'BTech-CS'
  
print(its1.stream) 
print(its2.stream)