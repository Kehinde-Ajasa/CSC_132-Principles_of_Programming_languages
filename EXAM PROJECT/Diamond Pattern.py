"""This program helps in drawing a diamond"""



def get_input():
    """Function to help get all user's input"""
    star = int(input("How big do you want the size of the diamond to be: "))
    return star



def top_part(stars):
    """Function to help display the upper part of the Diamond"""
    global jumper
    global width
    jumper = 1
    width = stars * 2
    for i in range(jumper, stars, 1):
        print((" *" * i).center(width, "-"))
    

def bottom_part(stars):
	"""Function to help display the bottom part of the Diamond"""
	for i in range(stars, jumper-1, -1):
		print((" *" * i).center(width, "-"))


top_part(get_input())
bottom_part(get_input())