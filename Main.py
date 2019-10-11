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

start = True
while start:
    begin = input("When you are ready to start enter 'y', if you're not ready enter anything else: ")
    if begin == 'y':
        start = False

print('Here we go!')
#gameRun to restart the again when finished
gameRun= True
while gameRun:
    playerScore = 0
    quest1= True
    while quest1:
        qu1= input("Question1: How many WOT books are there?" + "\n[a] 1 " + "\n[b] 5" +"\n[c] 15" + "\n[d] 10" + "\nAnswer: ")
        if qu1 != 'c':
            print("Sorry that is incorrect.")
        elif qu1 == 'c':
            playerScore += 1
            print("Correct!"+ " " + "your Score:", playerScore ,"out of 10")
            quest1 = False

    quest2= True
    while quest2:
        qu2= input("Question2: What is the title of book one?" + "\n[a] Wheel of Time" + "\n[b] Mars Attacks" + "\n[c] MistBorn" + "\n[d] The Way of Kings"+ "\nAnswer: ")
        if qu2 != 'a':
            print("sorry that is incorrect.")
        elif qu2 == 'a':
            playerScore += 1
            print("Correct!" + " " + "your Score:", playerScore , "out of 10")
            quest2 = False

    quest3= True
    qu3= input("Question3: ")

