"""This Program helps in printing out the pattern of a tree"""


def get_input():
    """This function gets the height of the tree from the user"""
    height_of_star = int(input('how big do u want the star'))
    return height_of_star


def top_part(height):
    """This function creates the tree and add the trunk to make it look nice"""
    star = "*"
    alignment = 100
    for i in range(height):
        print(star.center(alignment, ' '))
        star = star + "  *"
    trunk = '||||'
    for i in range(6):
        print(trunk.center(100))


print(top_part(get_input()))