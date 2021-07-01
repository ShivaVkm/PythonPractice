class PresidentOfIndia:
    def name(self):
        print("The president of India is Ram Nath Kovind")
    
    def gender(self):
        print("The president of India is Male")
    
    def work(self):
        print("""The primary duty of the president is to preserve, protect and 
        defend the constitution and the law of India per Article 60.""")


class PresidentOfUSA:
    def name(self):
        print("The president of India is Joe Biden")
    
    def gender(self):
        print("The president of India is Male")
    
    def work(self):
        print("""The president of the United States (POTUS) is the head of state and head of
         government of the United States of America. The president directs the executive branch
          of the federal government and is the commander-in-chief of the 
          United States Armed Forces.""")

poi = PresidentOfIndia()
poa = PresidentOfUSA()
for president in (poi, poa):
    president.name()
    president.gender()
    president.work()
    print()