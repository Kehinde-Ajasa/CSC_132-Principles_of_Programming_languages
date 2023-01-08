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

""""In python Try and Except are used in catching errors or bugs in codes here is how it works"""

"""Program for getting the amount of  term in an Arithmetic Progression"""
try:
    def get_inputs():
        """Section of code used to accept all user's inputs."""
        first_term = int(input("Enter the First Term: "))
        common_diff = int(input("Enter the Common Difference: "))
        last_term = int(input("Enter the Last Term: "))
        return first_term, common_diff, last_term


    def get_nth_term(values):
        """Main Logic of the project runs here"""
        amount_of_terms = 1
        my_data = list(values)
        for csc in range(my_data[0], my_data[2], my_data[1]):
            amount_of_terms += 1
        return amount_of_terms

    print(get_nth_term(get_inputs()))
except ValueError:
    def try_again():
        """Piece of code to help re-accept user's inputs"""
        print("Oops Invalid Input entered, Only Whole numbers are allowed. Try again")
        return get_inputs()
    print(try_again())

