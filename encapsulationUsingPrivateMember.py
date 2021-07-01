class LearnToCodeAndPractice:
    def __init__(self):
        self.__web1 = "GFG"   # __ (double underscores) represents to make the variables and methods private
        self.web2 = "HackerRank"  

class Programmer(LearnToCodeAndPractice):
    def __init__(self):
        LearnToCodeAndPractice.__init__(self)
        print("Calling the private members of the LearnToCodeAndPractice class")
        print(self.__web1)


lcp = LearnToCodeAndPractice()
print(lcp.web2)
p1 = Programmer()  # AttributeError: 'Programmer' object has no attribute '_Programmer__web1'
                    # because web1 instance variable is private
