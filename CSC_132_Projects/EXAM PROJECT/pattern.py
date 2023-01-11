"""This program helps in drawing different types of patterns by specifying the inputs and shapes to be drawn"""


def get_input():
    """Function to help get all user's input"""
    middle_star = int(input("How big do you want the size of your tree to be: "))
    return middle_star


# christmas Tree
def top_part(stars):
    """Function to help display the upper part of the star"""
    jumper = 1
    width = stars + 2
    for i in range(jumper, stars, 1):
    	print(("*" * i).center(width, ' '))

    for i in range(jumper, stars, 1):
    	print(("*" * 1).center(width, ' '))

top_part(get_input())