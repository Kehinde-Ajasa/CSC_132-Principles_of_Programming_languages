import random
import getpass
"""Description for the modules above"""

""" Random: The random module randomly selects a value from computer_game_options as the computers choice"""

"""getpass: To avoid players seeing each input while playing the game the getpass module allows players to enter their 
choice without displaying it """


def single_player(player_input):
    """This function compares player_input with the computers_choice and picks a winner """
    player_input_upper = player_input.upper()
    computer_game_options = ["ROCK", "PAPER", "SCISSORS"]
    computer_choice = random.choice(computer_game_options)
    if computer_choice == "ROCK":
        if player_input_upper == "ROCK":
            return "draw"
        elif player_input_upper == "PAPER":
            return "Paper covers Rock. You win"
        else:
            return "Rock smashes Scissors. You loose"
    elif computer_choice == "PAPER":
        if player_input_upper == "PAPER":
            return "draw"
        elif player_input_upper == "SCISSORS":
            return "Scissors cuts Paper. You win"
        else:
            return "Paper covers Rock. You loose"
    else:
        if player_input_upper == "SCISSORS":
            return "draw"
        elif player_input_upper == "ROCK":
            return "Rock smashes Scissors. You win"
        else:
            return "Scissors cuts Paper. You loose"


def multiplayer(player1, player2):
    """This function compares both players input and picks the winner """
    player1_upper = player1.upper()
    player2_upper = player2.upper()
    if player1_upper == "ROCK":
        if player2_upper == "ROCK":
            return "draw"
        elif player2_upper == "PAPER":
            return "Paper covers Rock. Player2 won"
        else:
            return "Rock smashes Scissors. Player1 won"
    elif player1_upper == "PAPER":
        if player2_upper == "PAPER":
            return "draw"
        elif player2_upper == "SCISSORS":
            return "Scissors cuts Paper. Player2 won"
        else:
            return "Paper covers Rock. Player1 won"
    elif player1_upper == "SCISSORS":
        if player2_upper == 'SCISSORS':
            return "draw"
        elif player2_upper == "ROCK":
            return "Rock smashes Scissors. Player2 won"
        else:
            return "Scissors cuts Paper. Player1 won"
    else:
        return "Enter proper value"


""" WELCOME TO ROCK PAPER SCISSORS WITH CONDITIONAL STATEMENTS """
print('Game Modes: "Enter 1 for single player", "Enter 2 for multiplayer player" \n')
game_mode = input('Enter game mode choice: ')
print('Enter "E" to end the game')
if game_mode == "1":
    while True:
        player_choice = input('Rock, Paper or Scissors: ')
        if player_choice.upper() == 'E':
            break
        else:
            print(single_player(player_choice))
elif game_mode == '2':
    while True:
        player1_choice = getpass.getpass(prompt="Player1 ROCK PAPER SCISSORS: ")
        player2_choice = getpass.getpass(prompt="Player2 ROCK PAPER SCISSORS: ")
        if player1_choice.upper() == "E" or player2_choice.upper() == "E":
            break
        else:
            print(multiplayer(player1_choice, player2_choice))
else:
    print('No game mode chosen')
