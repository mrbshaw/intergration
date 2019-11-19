# Robert Shaw
# trivia game based of the Wheel of time books
print("Welcome to My Trivia Game!")

# A function is a segment of code that performs a single task.
# input two numbers from 1 to 10 to get a lucky number.
def luckNumber():
    input_bad = True
    while input_bad:
        try:
            firstNumber = input("Enter a number between 1 and 10 to find your lucky number!: ")
            num1 = int(firstNumber)
            if num1 <= 10 and num1 >= 0:
                input_bad = False
            else:
                print("Number out of range or isn't a whole number, please try again")

        except ValueError:
            print("Number out of range or isn't a whole number, please try again")

    input_bad2 = True
    while input_bad2:
        try:
            secondNumber = input("Enter Another Number between 1 and 10: ")
            num2 = int(secondNumber)
            if num2 <= 10 and num2 >= 0:
                input_bad2 = False
            else:
                print("Number out of range or isn't a whole number, please try again")

        except ValueError:
            print("Number out of range or isn't a whole number, please try again")

    subt = num1 - num2
    print("Based on the numbers you entered, your lucky number is:", + subt)

def squareGame():
    l = int(input("Enter a Number: "))
    g = int(input("Enter another Number: "))
    for x in range(l):
        for x in range(g):
            print("*" + " ", end=" ")
        print()

def trivGame():
    # promt to begin game.
    start = True
    while start:
        begin = input("When you are ready to start enter 'y', if you're not ready enter anything else: ")
        if begin == 'y':
            start = False
    print('Here we go!' + "\nWheel of Time Trivia Game!")
    # gameRun to restart the again when finished
    gameRun = True
    while gameRun:
        playerScore = 0
        quest1 = True
        while quest1:
            qu1 = input(
                "Question1: How many WOT books are there?" + "\n[a] 1 " + "\n[b] 5" + "\n[c] 15" + "\n[d] 10" + "\nAnswer: ")
            if qu1 != 'c':
                print("Sorry that is incorrect.")
            elif qu1 == 'c':
                playerScore += 1
                print("Correct!" + " " + "your Score:", playerScore, "out of 10")
                quest1 = False

        quest2 = True
        while quest2:
            qu2 = input(
                "Question2: What is the title of book one?" + "\n[a] Eye of the World" + "\n[b] Mars Attacks" + "\n[c] MistBorn" + "\n[d] The Way of Kings" + "\nAnswer: ")
            if qu2 != 'a':
                print("sorry that is incorrect.")
            elif qu2 == 'a':
                playerScore += 1
                print("Correct!" + " " + "your Score:", playerScore, "out of 10")
                quest2 = False
        # add a way for user only haves a 3 temp
        quest3 = True
        while quest3:    
            qu3 = input(
                "Question3: In the book,The Eye of the world, which character says, In wars,boy, fools kill other fools for foolish causes. ?" + "\n[a] Min Farshaw" + "\n[b] Rand al'Thor" + "\n[c] Thom Merrilin" + "\n[d] Lanfear" + "\nAnswer: ")
            if qu3 != 'c':
                print("Sorry that is incorrect")
            elif qu3 == 'c':
                playerScore += 1
                print("Correct!" + " " + "your Score:", playerScore, "out of 10")
                quest3 = False

        quest4 = True
        while quest4:
            qu4 = input("Question4: Who is the Dragon reborn?" + "\n[a] Min Farshaw" + "\n[b] Rand al'Thor" + "\n[c] Thom Merrilin" + "\n[d] Lanfear" + "\nAnswer: ")
            if qu3 != 'c':
                print("Sorry that is incorrect")
            elif qu4 == 'b':
                playerScore += 1
                print("Correct!" + " " + "your Score:", playerScore, "out of 10")
                quest4 = False

        quest5 = True
        while quest5:
            qu5= input(" Question5: Who finished the last two books?" + "\n[a] Robert Jordon" + "\n[b] Brandon Sanderson "+ "\n[c] Robert Shaw " + "\n[d] Tony the Tiger " + "\nAnswer: ")
            if qu5 != 'b':
                print("Sorry that is incorrect")
            elif qu5== 'b':
                playerScore += 1
                print("Correct!" + " " + "your Score:", playerScore, "out of 10")
                quest5 = False

        quest6 = True
        while quest6:
            qu6 = input(
                "Question6: Do Myrddraal have eyes ?" + "\n[a] Yes " + "\n[b] No " + "\nAnswer: ")
            if qu6 != 'b':
                print("Sorry that is incorrect")
            elif qu6 == 'b':
                playerScore += 1
                print("Correct!" + " " + "your Score:", playerScore, "out of 10")
                quest6 = False

        quest7 = True
        while quest7:
            qu7 = input(
                "Question7: Who made the Trollocs?" + "\n[a] Aginor " + "\n[b] Ishamael " + "\n[c] Balthamel " + "\n[d] Demandred " + "\nAnswer: ")
            if qu7 != 'a':
                print("Sorry that is incorrect")
            elif qu7 == 'a':
                playerScore += 1
                print("Correct!" + " " + "your Score:", playerScore, "out of 10")
                quest7 = False

        quest8 = True
        while quest8:
            qu8 = input(
                "Question8: My name was once Lillen Moiral, but now I am know as... ?" + "\n[a] Mesaana " + "\n[b] Semirhage " + "\n[c] Lanfear " + "\n[d] Moghedien " + "\nAnswer: ")
            if qu8 != 'd':
                print("Sorry that is incorrect")
            elif qu8 == 'd':
                playerScore += 1
                print("Correct!" + " " + "your Score:", playerScore, "out of 10")
                quest8 = False

        quest9 = True
        while quest9:
            qu9 = input(
                "Question9: Title of the last book?" + "\n[a] The Eye of the World " + "\n[b] A Memory of Light " + "\n[c] The Shining " + "\n[d] Dance Party boogalo " + "\nAnswer: ")
            if qu9 != 'b':
                print("Sorry that is incorrect")
            elif qu9 == 'b':
                playerScore += 1
                print("Correct!" + " " + "your Score:", playerScore, "out of 10")
                quest9= False

        quest10 = True
        while quest10:
            qu10 = input(
                "Question10:How many wifes did the Dragon have at the end of the books?" + "\n[a] 2 " + "\n[b] 3 " + "\n[c] 4 " + "\n[d] 2 " + "\nAnswer: ")
            if qu10 != 'b':
                print("Sorry that is incorrect")
            elif qu10 == 'b':
                playerScore += 1
                print("Correct!" + " " + "your Score:", playerScore, "out of 10")
                quest10 = False
        print("You have completed the game!" + "\nFinal score: " , playerScore)
        playagain = input("Type 'y' to play again, type anything else to return to menu"+ "\nEnter: ")
        if playagain != 'y':
            gameRun= False
        else:
            trivGame()

# Put lucky number code and triva game in different functions to make a slection menu.
runMenu = True
while runMenu:
    print("Enter Choice")
    print("1. Find your Lucky number")
    print("2. Play Trivia Game")
    print("3. Make a square")
    print("4. Quit")
    selection = int(input("Enter: "))
    if selection == 1:
        luckNumber()
    elif selection == 2:
        trivGame()
    elif selection ==3:
        squareGame()
    elif selection == 4:
        runMenu = False

