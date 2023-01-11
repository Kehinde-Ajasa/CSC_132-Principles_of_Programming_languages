"""Recursion is a term in programming used to explain functions that call itself"""
"""All functions, after being created have a particular way in which they are being called
sometimes you might want a section of code (a function) perform a specific task over and over
again. To do this, you can loop the function again and again or create a function where it
calls itself."""


"""This is an example of a recursive function to calculate the factorial of a number"""


def recursion(number):
    """Recursive function to help print the factorial of a particular number"""
    if number == 1:
        return 1  # The function return 1 if the user's input is 1
    else:
        return number * recursion(number - 1)  # Here is where recursion occurs,
"""The function recursion returns a number, if the number is not equal to 1, the function
does not stop running. the outputs of the number continues getting multiplied to the output
of the previous call, there by creating a self-calling means of the concept RECURSION"""


user_input = int(input("Please Enter the number: "))
print(recursion((user_input)))
