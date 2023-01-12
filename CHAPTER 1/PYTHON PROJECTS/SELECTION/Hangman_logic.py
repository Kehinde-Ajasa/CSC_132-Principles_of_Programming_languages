"""
A prisoner has been captured and ready to be executed
However, he has a chance to free himself by Guessing a random number from 1 to 30
He is hanged gradually as he fails; he has just 6 trials
There's always a hint for him, whether to guess lower or higher
"""
# This is the module that gives us a random value; just as its name implies
import random
# This isn't a module really; it's just a Python file that contains
# the Hanging Descriptions we'll be using
import Hangman_diagram as hg
# this will help us get a random number from 1-30
# randint means random integer
random_value = random.randint(1, 30)

# Initializing the numbers of guesses the prisoner has done
guesses = 0

# for this project, we're using a while loop;
# "while True" means, keep running this loop until you find a break
# meaning, the loop will keep running until it's False
while True:
    # Getting the user's input
    user_guess = int(input("Enter a Number from 1-30: "))

    # After every guess, we want this guesses variable to increase by one
    guesses = guesses + 1
    # Now, we're going to write some basic conditions for or input (user_guess)

    # Since we want the guess to be between 1 and 30
    # an input less than or greater than 1 or 30 respectively should be invalid
    if user_guess < 0:
        print("Invalid number, enter a Number from 1-30")
    elif user_guess > 30:
        print("Invalid number, enter a Number from 1-30")

    # this is the set of conditions that checks if the user input is accurate
    # or otherwise

    elif user_guess > random_value:
        # The user has guessed already; but it's invalid;
        # we just want to print the Hanging description that goes with the nth guess.
        if guesses == 1:
            print(hg.hanged[0])
        elif guesses == 2:
            print(hg.hanged[1])
        elif guesses == 3:
            print(hg.hanged[2])
        elif guesses == 4:
            print(hg.hanged[3])
        elif guesses == 5:
            print(hg.hanged[4])
        elif guesses == 6:
            print(hg.hanged[5])
            # and when you guess 6 times incorrectly?
            # The prisoner dies, and the loop breaks too
            print("You Died!")
            break
        print("Guess Lower")

    # This is just the same as the first...
    elif user_guess < random_value:
        if guesses == 1:
            print(hg.hanged[0])
        elif guesses == 2:
            print(hg.hanged[1])
        elif guesses == 3:
            print(hg.hanged[2])
        elif guesses == 4:
            print(hg.hanged[3])
        elif guesses == 5:
            print(hg.hanged[4])
        elif guesses == 6:
            print(hg.hanged[5])
            print("You Died!")
            break
        print("Guess Higher")
    else:
        print("You won\nTotal Guesses: ", guesses)
        break

"""
There are many ways to solve a challenge, and this is just my own solution.
You can challenge yourself by writing a shorter code that does the same thing as this
Or, instead of making the user guess, why not make the computer guess till it gets it?
"""
