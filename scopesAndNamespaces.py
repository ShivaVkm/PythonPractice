# This I learnt from python's official docs tutorial and I implemented it at my own

def scopeTest():

    def doLocal():
        spam = "This is the local spam."

    def doNonLocal():
        nonlocal spam
        spam = "This is the non-local spam."
    
    def doGlobal():
        global spam
        spam = "This is the global spam."

    spam = "This is the test spam"
    doLocal()
    print("After local method ,",spam)
    doNonLocal()
    print("After non-local method ,",spam)
    doGlobal()
    print("After global method ,",spam)


scopeTest()
print("The spam's value in the global scope,",spam)