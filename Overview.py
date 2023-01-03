"""This file contains the combined version of all unit files/modules in the repository"""

# Project 1
"""This code is the master code for all CSC 132 terminologies"""

# Introduction to data abstraction


"""Data abstraction or encapsulation is a programming language principle of hiding data 
using functions, libraries and modules, this gives room for flexibility of programmers
and writing readable and clean codes."""


def get_range(user_list):
    """This function is used to get the range of a particular set of data (numbers)."""

    def get_max_num(user_list):
        """This function is used to get the highest number in a given set of data"""
        max_val = 0
        for number in user_list:
            if number > max_val:
                max_val = number
            else:
                max_val = max_val

        return max_val

    def get_min_num(user_list):
        """This function is used to get the lowest number in a given set of data"""
        min_val = get_max_num(user_list)
        for value in user_list:
            if value < min_val:
                min_val = value
            else:
                min_val = min_val

        return min_val

    d_range = get_max_num(user_list) - get_min_num(user_list)

    return f'The range of the values {user_list} is {d_range}'


# Project 2
from abstracted_data import get_range

"""It is already established that a self contained code-based was created,
this self contained code-base is known as a MODULE and it is going to be our
stater tool for our data abstraction concept."""


def user_input():
    """Accepting all user's input"""
    length_of_list = int(input("How many numbers are you given: "))
    user_list = list()
    for i in range(length_of_list):
        number = int(input(f"Enter your {i + 1} number: "))
        user_list.append(number)

    return user_list


print(get_range(user_input()))

"""In this piece of code, the user gets to input the numbers present in 
a list for the program to get the range of the given data. There are 3
unique things here
1. The code despite having alot of computation is clean
2. The working principle of how the range is gotten is not disclosed
3. As a result of this, programmers are given more flexibility while programming
because the piece of code (abstracted data) can be used anywhere in the software creation"""


# Project 3
"""Aliasing is a loop hole in programming that treatens the reliability of codes
when written. It is a concept used to explain the phenomenon that exists
when two different memory location contains the same data"""


def Aliasing():
    first_number = 80
    second_number = first_number
    """The assignment of the second_number to the first number is termed aliasing
    and the main disadvantage is that if the second_number is edited or deleted, it
    affects the first number value of 80, which makes the code no longer safe."""
    pass
    """To prevent this multiple reference creation is prohibited"""

    """This module helps in checking if a number is prime or not.
    Prime numbers are numbers that can only divide 1 and itself without reminder
    examples are 2, 3, 5 etc"""
    """How it works
    This module accepts a user input and loops through all number from 2 to that input
     then divides the user input by all numbers gotten from the loop.
     it adds this result to a list, if 0 is in the list, user_input is Not prime, if 0 is not
     user input is prime"""


# Project 4
def is_prime_number(user_input):
        """An approach to check if a number is prime or not."""
        remainder_list = list()
        if user_input == 2:
            return 1
        else:
            for i in range(2, user_input):
                remainder_list.append(user_input % i)  # adding the remainder of the loop to a list
            if 0 in remainder_list:
                return 0  # false the user_number is not a prime number
            else:
                return 1  # True the user_number is a prime number

"""This program helps in multiplying an amount of prime numbers
program must first check if number entered by user are prime or not"""

# Project 5
def user_input():
    """Accepting all user's input and performing operation"""
    product = 1
    prime_number_list = list()
    amount_of_numbers = int(input("How many prime numbers do you want to multiply: "))
    for i in range(1, amount_of_numbers + 1):
        p_number = int(input(f"Enter your {i} number: "))
        while (is_prime_number(p_number)) != 1:
            print("The number you entered is not a prime number, Try again")
            p_number = int(input(f"Enter your {i} number: "))
        if is_prime_number(p_number) == 1:
            prime_number_list.append(p_number)
            product *= p_number

    return f'The Product of the prime numbers {prime_number_list} is {product}'

print(user_input())

