"""In the design of programming Languages, its very important that in the construction
of programming languages, a very key concept is added into considerations."""

"""Reliability is a very important concept because it shows how much a programming language
can be reliable in terms of error handling and type checking"""

"""When codes are written, there is tendency for the codes to contain errors (also known
as bugs) these errors disallows the program to run as intended. but the most interesting
thing is that these errors are not always visible by the users in a large system design."""

"""The reason is because these errors have been predicted to happen and has been caught by the 
developer. If a programming language would not be reliable these errors would never have
been caught"""

""""In Python Try and Except are used in catching errors or bugs in codes here is how it works"""
"""Program for getting the amount of  term in an Arithmetic Progression"""


def get_inputs():
    """Section of code used to accept all user's inputs."""
    global first_term, common_diff, last_term

    try:
        first_term = int(input("Enter the First Term: "))
        common_diff = int(input("Enter the Common Difference: "))
        last_term = int(input("Enter the Last Term: "))

    except ValueError:
        print("Oops the value you have entered is not allowed, only whole numbers are allowed")
        get_inputs()
    return first_term, common_diff, last_term


def amount_of_terms(values):
    """Main Logic of the project runs here"""
    number_of_terms = 1
    my_data = list(values)
    for csc in range(my_data[0], my_data[2], my_data[1]):  # First term, last term, common_difference
        number_of_terms += 1
    return f'From {my_data[0]} to {my_data[2]} there are {number_of_terms} terms in the A.P'


print(amount_of_terms(get_inputs()))
