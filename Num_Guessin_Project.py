import random
import sys

import matplotlib.pyplot as plt
import numpy as np
# Importing Key Libraries Above /\

count = 0
xCoords = []
yCoords = []
userInputTwo = 0
graphUserInput = ""
# Setting Key Reused Variables Above /\

def resetKeyValues():
    global count
    global xCoords
    global yCoords
    count = 0
    xCoords = []
    yCoords = []
# Reset reappearing key global values /\

# Abstraction \/
def boundAndRoundChecker(userInput, lowerBound, upperBound):
    if lowerBound > upperBound or lowerBound > userInput or userInput > upperBound or userInput != round(userInput):
        # The above statement checks if the ranges are appropriate, user input is contained within the range,
        # and that the user input in a integer value /\
        sys.exit("Please Try again... Either check to make sure that your lowerbound:" + " " + str(
            lowerBound) + " " + "is less than your upperbound:" + " " + str(
            upperBound) + " or that your guess:" + " " + str(
            userInput) + " " + "is an integer contained within them and restart the tool")
# Checks if the user's inputted values are logical and will not result in program failure /\

# Child Algorithm 2 \/
def graphAndCountAndCompGuessUpdater(lowerBound, upperBound, compGuess):
    global count
    global xCoords
    global yCoords
    # Accesses global variables, which must be done before trying to use them within this function(sequencing) /\
    xCoords.append(count + 1)
    yCoords.append(compGuess)
    # Updates them appropriately for each method/\
    compGuess = random.randint(lowerBound, upperBound)
    count += 1
    # Updates count using '+' mathematical operator /\
    # Updates key values that are used in both guessing methods /\

# Child Algorithm 1 \/
def graphingItems(userInput, compGuess):
    global graphUserInput
    graphUserInput = input("Do you want a graph?(Y/N)")
    if graphUserInput == "Y":
        xCoords.append(count + 1)
        yCoords.append(compGuess)
        # Adds computer guess and count values to lists /\
        x = np.linspace(0, xCoords[-1], len(xCoords))
        y = 0 * x + userInput
        plt.plot(xCoords, yCoords, 'g', label='Computer Guesser', linewidth=2.0, alpha=0.8)
        plt.plot(x, y, '-r', label=' User Input=' + " " + str(userInput), linewidth=2.0, alpha=0.6)
        # Plots user input and computer guesser lines /\
        plt.legend(loc='upper left')
        # Positions legend /\
        plt.xlabel('The Number of Guesses(Wow, it took' + " " + str(count + 1) + " " "attempts!)", color='#1C2824')
        plt.ylabel('The Value of Guesses', color='#1C2824')
        plt.title('How to make sense of my program')
        # Labels graph appropriately /\
        plt.scatter(xCoords, yCoords, s=15)
        # Draws guesser lines for more vivid visualization /\
        plt.grid()
        plt.show()
        # Helps open a separate window displaying graph and enables grid /\
    # Uses logical operator "==" to check if user desires a graph or not /\
    else:
        print("You choose no graph, so look at boring logs now ;( ")
    # Uses if/else statements to check if user wants a graph or not(selection) /\
# Contains all processes related to the generalized graphing for my methods/\

# Parent Algorithm(Contains Abstraction) \/
def guesserOne():
    # Acquires user input in an user friendly way \/
    userInput = int(input("What is your secret Number?[Method 1] "))
    lowerBound = int(input("What will be the computer guesser's lower limit?[Method 1] "))
    upperBound = int(input("What will be the computer guesser's upper limit?[Method 1] "))
    # Abstraction in action \/
    boundAndRoundChecker(userInput, lowerBound, upperBound)
    compGuess = random.randint(lowerBound, upperBound)
    # Checks for valid input and updates computer's guess /\
    global count
    while compGuess != userInput:
        # Runs till the guessed value is equal to user value /\
        if compGuess > userInput:
            print("Attempt" + " " + str(count + 1) + ":" + str(float(compGuess)) + " = This is too high")
            # Child Algorithm 2 \/
            graphAndCountAndCompGuessUpdater(lowerBound, upperBound, compGuess)
            # Shrinks the upper bound appropriately if computer guesses too high and updates some key values /\
            upperBound = compGuess
            compGuess = random.randint(lowerBound, upperBound)

        if compGuess < userInput:
            print("Attempt" + " " + str(count + 1) + ":" + str(float(compGuess)) + " = This is too low")
            # Child Algorithm 2 \/
            graphAndCountAndCompGuessUpdater(lowerBound, upperBound, compGuess)
            # Raises the lower bound appropriately if computer guesses too low and updates some key values /\
            lowerBound = compGuess
            compGuess = random.randint(lowerBound, upperBound)

    global xCoords
    global yCoords
    print(str(userInput) + " = Awesome, it took" + " " + str(count + 1) + " " "tries")
    # Child Algorithm 1 \/
    graphingItems(userInput, compGuess)
    # Utilizes global variables, updates them appropriately and displays them in graph /\
    resetKeyValues()
    # Resets the key global variables /\

# Secondary Parent Algorithm(Also contains abstraction/algorithms)
def guesserTwo():
    # Acquires user input in an user friendly way \/
    userInput = int(input("What is your secret Number?[Method 2] "))
    lowerBound = int(input("What will be the computer guesser's lower limit?[Method 2] "))
    upperBound = int(input("What will be the computer guesser's upper limit?[Method 2] "))
    # Abstraction in action \/
    boundAndRoundChecker(userInput, lowerBound, upperBound)
    compGuess = random.randint(lowerBound, upperBound)
    # Checks for valid input and updates computer's guess /\
    global count
    while compGuess != userInput:
        # Runs till the guessed value is equal to user value /\
        if compGuess > userInput:
            print("Attempt" + " " + str(count + 1) + ":" + str(float(compGuess)) + " = This is too high")
            # Child Algorithm 2 \/
            graphAndCountAndCompGuessUpdater(lowerBound, upperBound, compGuess)
            # Updates key values, but does not modify range /\
            compGuess = random.randint(lowerBound, upperBound)
        elif compGuess < userInput:
            print("Attempt" + " " + str(count + 1) + ":" + str(float(compGuess)) + " = This is too low")
            # Child Algorithm 2 \/
            graphAndCountAndCompGuessUpdater(lowerBound, upperBound, compGuess)
            # Updates key values, but does not modify range /\
            compGuess = random.randint(lowerBound, upperBound)
    global xCoords
    global yCoords
    print(str(userInput) + " = Awesome, it took" + " " + str(count + 1) + " " "tries")
    # Child Algorithm 1 \/
    graphingItems(userInput, compGuess)
    # Utilizes global variables, updates them appropriately and displays them in graph /\
    resetKeyValues()
    # Resets the key global variables /\

while userInputTwo != str("Quit"):
    # Runs till user wants to stop /\
    userInputTwo = input(
        "Pick a random number and the computer must guess... Use Method 1 or 2?(Type number), or maybe 'Quit'? ")
    if userInputTwo == str("1"):
        guesserOne()
    elif userInputTwo == str("2"):
        guesserTwo()
    else:
        print("...")
    # Calls each method based on user input or print epsilons if user does anything else /\
print("Thanks for testing!")
'''Finally thanks the user for utilizing the tool'''
