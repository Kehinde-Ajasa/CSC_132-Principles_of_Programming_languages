"""Aliasing is a loop hole in programming that treatens the reliability of codes
when written. It is a concept used to explain the phenomenon that exists
when two different memory location contains the same data"""


def Aliasing():
    first_number = 80
    second_number = first_number
    """The assignment of the second_number to the first character_change is termed aliasing
    and the main disadvantage is that if the second_number is edited or deleted, it
    affects the first character_change value of 80, which makes the code no longer safe."""
    pass
    """To prevent this multiple reference creation is prohibited"""