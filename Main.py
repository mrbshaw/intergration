"""
This is my main file for this program.
__author__ = Robert Shaw Jr.
Code from Prof. Van. AND Python Activity 1 -13.
"""
# Trivia game based of the Wheel of time books.
print("Welcome to My Trivia Game!")


# A function is a segment of code that performs a single task.
def run_pay():
    def compute_pay(hrs, rt):
        if hrs > 40:
            reg = fh * fr
            otp = (fh - 40.0) * (fr * 0.5)
            pay = reg + otp
        else:
            pay = fh * rt
        return pay

    hrs = input("Enter Hours:")
    rt = input("Rate of Pay: ")
    fh = float(hrs)
    fr = float(rt)
    pay = compute_pay(fh, fr)
    print(pay)


# Input two numbers from 1 to 10 to get a lucky number.


def luck_number():
    """
    Try and except example. makes sure inputs are between the 1 and 10 and 
    then adds the two numbers together.

    """

    input_bad = True
    while input_bad:
        try:
            first_number = input(
                "Enter a number between 1 and 10 to find your "
                "lucky number!: ")
            num1 = int(first_number)
            if 10 >= num1 >= 0:
                input_bad = False
            else:
                print(
                    "Number out of range or isn't a whole number, please try "
                    "again")

        except ValueError:
            print(
                "Number out of range or isn't a whole number, please try again"
            )

    input_bad2 = True
    while input_bad2:
        try:
            second_number = input("Enter Another Number between 1 and 10: ")
            num2 = int(second_number)
            if 10 >= num2 >= 0:
                input_bad2 = False
            else:
                print(
                    "Number out of range or isn't a whole number, please try "
                    "again")

        except ValueError:
            print(
                "Number out of range or isn't a whole number, please try again"
            )

    subt = num1 - num2
    print("Based on the numbers you entered, your lucky number is:", + subt)


# funcation to run code that prints "*" in the range inputed by user.

def square_game():
    """
    For range loop in print statements.
    """
    l = int(input("Enter a Number: "))
    w = int(input("Enter another Number: "))
    for x in range(l):
        for x in range(w):
            print("*" + " ", end=" ")
        print()


def triv_game():
    """
    put quiz game in a function so I could call the it to start the game.

    """
    # promt to begin game.
    start = True
    while start:
        begin = input("When you are ready to start enter 'y', if you're not "
                      "ready enter anything else: ")
        if begin == 'y':
            start = False
    print('Here we go!' + "\nWheel of Time Trivia Game!")
    # game_Run to restart the again when finished
    game_Run = True
    while game_Run:
        player_score = 0
        quest_1 = True
        while quest_1:
            qu_1 = input(
                "Question1: How many WOT books are there?" + "\n[a] 1 " +
                "\n[b] 5" + "\n[c] 15" + "\n[d] 10" + "\nAnswer: ")
            if qu_1 != 'c':
                print("Sorry that is incorrect.")
            elif qu_1 == 'c':
                player_score += 1
                print("Correct!" + " " + "your Score:", player_score,
                      "out of 10")
                quest_1 = False

        quest_2 = True
        while quest_2:
            qu_2 = input(
                "Question2: What is the title of book one?" +
                "\n[a] Eye of the World" + "\n[b] Mars Attacks" + "\n[c] "
                                                                  "MistBorn "
                + "\n[d] The Way of Kings" + "\nAnswer: ")
            if qu_2 != 'a':
                print("sorry that is incorrect.")
            elif qu_2 == 'a':
                player_score += 1
                print("Correct!" + " " + "your Score:", player_score,
                      "out of 10")
                quest_2 = False

        quest_3 = True
        while quest_3:
            qu_3 = input(
                "Question3: In the book,The Eye of the world, which character "
                "says, In wars,boy, fools kill other fools for foolish "
                "causes. ? "
                + "\n[a] Min Farshaw" + "\n[b] Rand al'Thor" + "\n[c] Thom "
                                                               "Merrilin "
                + "\n[d] Lanfear" + "\nAnswer: ")
            if qu_3 != 'c':
                print("Sorry that is incorrect")
            elif qu_3 == 'c':
                player_score += 1
                print("Correct!" + " " + "your Score:", player_score,
                      "out of 10")
                quest_3 = False

        quest_4 = True
        while quest_4:
            qu_4 = input("Question4: Who is the Dragon reborn?" +
                         "\n[a] Min Farshaw" + "\n[b] Rand al'Thor" +
                         "\n[c] Thom Merrilin" + "\n[d] Lanfear" + "\nAnswer: "
                         )
            if qu_4 != 'c':
                print("Sorry that is incorrect")
            elif qu_4 == 'b':
                player_score += 1
                print("Correct!" + " " + "your Score:", player_score,
                      "out of 10")
                quest_4 = False

        quest_5 = True
        while quest_5:
            qu_5 = input(" Question5: Who finished the last two books?"
                         + "\n[a] Robert Jordon" + "\n[b] Brandon Sanderson "
                         + "\n[c] Robert Shaw " + "\n[d] Tony the Tiger " +
                         "\nAnswer: ")
            if qu_5 != 'b':
                print("Sorry that is incorrect")
            elif qu_5 == 'b':
                player_score += 1
                print("Correct!" + " " + "your Score:", player_score,
                      "out of 10")
                quest_5 = False

        quest_6 = True
        while quest_6:
            qu_6 = input(
                "Question6: Do Myrddraal have eyes ?" + "\n[a] Yes " + "\n["
                                                                       "b] "
                                                                       "No "
                + "\nAnswer: ")
            if qu_6 != 'b':
                print("Sorry that is incorrect")
            elif qu_6 == 'b':
                player_score += 1
                print("Correct!" + " " + "your Score:", player_score,
                      "out of 10")
                quest_6 = False

        quest_7 = True
        while quest_7:
            qu_7 = input(
                "Question7: Who made the Trollocs?" + "\n[a] Aginor "
                + "\n[b] Ishamael " + "\n[c] Balthamel " + "\n[d] Demandred "
                + "\nAnswer: ")
            if qu_7 != 'a':
                print("Sorry that is incorrect")
            elif qu_7 == 'a':
                player_score += 1
                print("Correct!" + " " + "your Score:", player_score,
                      "out of 10")
                quest_7 = False

        quest_8 = True
        while quest_8:
            qu_8 = input(
                "Question8: My name was once Lillen Moiral, but now I am "
                "know as... ? "
                + "\n[a] Mesaana " + "\n[b] Semirhage " + "\n[c] Lanfear " +
                "\n[d] Moghedien " + "\nAnswer: ")
            if qu_8 != 'd':
                print("Sorry that is incorrect")
            elif qu_8 == 'd':
                player_score += 1
                print("Correct!" + " " + "your Score:", player_score,
                      "out of 10")
                quest_8 = False

        quest_9 = True
        while quest_9:
            qu_9 = input(
                "Question9: Title of the last book?" + "\n[a] The Eye of the "
                                                       "World "
                + "\n[b] A Memory of Light " + "\n[c] The Shining " +
                "\n[d] Dance Party boogalo " + "\nAnswer: ")
            if qu_9 != 'b':
                print("Sorry that is incorrect")
            elif qu_9 == 'b':
                player_score += 1
                print("Correct!" + " " + "your Score:", player_score,
                      "out of 10")
                quest_9 = False

        quest_10 = True
        while quest_10:
            qu_10 = input(
                "Question10:How many wifes did the Dragon have at"
                " the end of the books?" + "\n[a] 2 " + "\n[b] 3 " + "\n[c] 4 "
                + "\n[d] 2 " + "\nAnswer: ")
            if qu_10 != 'b':
                print("Sorry that is incorrect")
            elif qu_10 == 'b':
                player_score += 1
                print("Correct!" + " " + "your Score:", player_score,
                      "out of 10")
                quest_10 = False
        print("You have completed the game!" + "\nFinal score: ", player_score)
        play_again = input(
            "Type 'y' to play again, type anything else to return"
            " to menu" + "\nEnter: ")
        if play_again != 'y':
            game_Run = False
        else:
            triv_game()


# Put lucky number code and triva game in different functions to make a
# selection menu.
run_menu = True
while run_menu:
    print("Enter Choice")
    print("1. Find your Lucky number")
    print("2. Play Trivia Game")
    print("3. Make a square")
    print("4. Check rate of Pay")
    print("5. Quit")
    selection = int(input("Enter: "))
    if selection == 1:
        luck_number()
    elif selection == 2:
        triv_game()
    elif selection == 3:
        square_game()
    elif selection == 4:
        run_pay()
    elif selection == 5:
        run_menu = False
