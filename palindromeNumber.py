# A number that remains the same after its digits are reversed is called a palindrome number


number = int(input("Enter a number:"))
temporaryNumber = number
reversedNumber = 0
while(number > 0):
    digit = number % 10 
    reversedNumber = reversedNumber * 10 + digit
    number = number // 10

if(temporaryNumber == reversedNumber):
    print("The number is a palindrome number.")
else:
    print("The number is not a palindrome number.")
