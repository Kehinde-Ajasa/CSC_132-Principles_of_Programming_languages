"""
Rock-Paper-Scissors is a Two-man Physical Game.
The two players are supposed to do a sign with one of their Hands at the call of Rock-Paper-Scissors shoot!
Fist for Rock, Flat hand for paper and two middle fingers for Scissors.

Rock crushes Scissors, Scissors cuts Paper and Paper covers Rock.
"""
# The random is used for any Random operations we're dealing with...
import random


# This is the function responsible for playing the Game.
# player_choice is the variable that represents the choice of the Player;
# The run_game function will be called at the end of this Code;
# Then player_choice will be passed as a Parameter.
def run_game(player_choice):
    print("Rock Paper Scissors; Shoot!")
    # The .choice() method picks one of values in the Array at Random
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    # Here; we're using a formatted string; this made us be able to write the 
    # whole expression as a sentence.
    print(f"You chose {player_choice} and Computer chose {computer_choice}")
    
    # This is the set(s) of conditions that is responsible for winning
    # Notice that the conditions for winning follows the same Rules as the little note on line 6
    # Again, notice that the lines are conditions are separated with a backward slash; its this way for 2 reasons
    # 1. The coding convention for maximum number of characters in a line is 79 (PEP-8)
    # Go to https://peps.python.org/pep-0008 to read more
    # 2. It makes our code easier to read.
    if \
        (computer_choice == "Rock" and player_choice == "Scissors")\
        or (computer_choice == "Scissors" and player_choice == "Paper")\
            or (computer_choice == "Paper" and player_choice == "Rock"):
        return "Computer Won"
    # same thing as the above set of conditions
    elif (player_choice == "Rock" and computer_choice == "Scissors")\
        or (player_choice == "Scissors" and computer_choice == "Paper")\
            or (player_choice == "Paper" and computer_choice == "Rock"):
        return "You won!"
    # And if nobody wins; its means they chose the same thing, and it's a TIE
    else:
        return "It was a Tie!"


print("Rock; Paper and Scissors")
# Gets the choice of the Player
choice = input("Make a choice> ")
# Then we invoke the run_game function with Player's choice passed as the Parameter
print(run_game(choice))
