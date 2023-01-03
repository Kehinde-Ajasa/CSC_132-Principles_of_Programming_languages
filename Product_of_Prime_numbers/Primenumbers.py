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
    return sum([1 if user_input%q == 0 else 0 for q in range(1, user_input+1)]) == 2
