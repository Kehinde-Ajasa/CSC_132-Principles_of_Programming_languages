"""This module helps in checking if a number is prime or not.
Prime numbers are numbers that can only divide 1 and itself without reminder
examples are 2, 3, 5 etc"""
"""How it works
This module accepts a user input and loops through all number from 2 to that input
 then divides the user input by all numbers gotten from the loop.
 it adds this result to a list, if 0 is in the list, user_input is Not prime, if 0 is not
 user input is prime"""


def is_prime_number(user_input):
    """An approach to check if a number is prime or not."""
    remainder_list = list()
    if user_input == 2:
        return 1
    else:
        for i in range(2, user_input):
            remainder_list.append(user_input % i)  # adding the remainder of the loop to a list
        if 0 in remainder_list:
            return 0  # false the user_number is not a prime character_change
        else:
            return 1  # True the user_number is a prime character_change
