"""This program helps in drawing a diamond"""



def get_input():
    """Function to help get all user's input"""
    star = int(input("How big do you want the size of the diamond to be: "))
    character = input("What letter or character do you want your diamond to be in: ")
    if len(character) > 1:
        return "Invalid character entered the values of the character can only be 1 letter long"
    else:
        return star, character



def top_part(stars):
    """Function to help display the upper part of the Diamond"""
    global jumper
    global width
    jumper = 1
    width = stars[0] * 2
    for i in range(jumper, stars[0], 1):
        print((f" {stars[1]}" * i).center(width, "-"))
    

def bottom_part(stars):
	"""Function to help display the bottom part of the Diamond"""
	for i in range(stars[0], jumper-1, -1):
		print((f" {stars[1]}" * i).center(width, "-"))


top_part(get_input())
bottom_part(get_input())