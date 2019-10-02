#Robert Shaw
#trivia game based of the Wheel of time books
print("Welcome to My Trivia Game!")

while True:
    firstNumber = input("Enter a number between 1 and 10 to find your lucky number!: ")
    num1 = int(firstNumber)
    if num1 <= 10 and num1 >= 0:
        break
    else:
        print("Number out of range, please try again")

while True:
    secondNumber=input("Enter Another Number between 1 and 10: ")
    num2 = int(secondNumber)
    if num2 <= 10 and num2 >= 0:
        break
    else:
        print("Number out of range, please try again")
subt = num1 - num2
print("Based on the numbers you entered, your lucky number is:", + subt)

