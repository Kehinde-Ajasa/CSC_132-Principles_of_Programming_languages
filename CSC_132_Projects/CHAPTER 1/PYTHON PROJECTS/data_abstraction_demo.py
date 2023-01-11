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

