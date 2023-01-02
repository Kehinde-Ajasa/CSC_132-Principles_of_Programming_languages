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
