"""This program helps in drawing different types of patterns by specifying the inputs and shapes to be drawn"""


# This draws the diamond pattern


def get_input():
    """Function to help get all user's input"""
    middle_star = 9#int(input("How many stars do you want the middle of your diamond to contain: "))
    return middle_star

print(get_input())


def top_part(stars):
    """Function to help display the upper part of the star"""
    jumper = 1
    for i in range(jumper, stars, 1):
    	print(" * " * i)

top_part(get_input())