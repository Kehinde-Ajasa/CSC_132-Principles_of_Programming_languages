
for i in range(5):
    print(i)
# in the above loop, i is the loop variable because it represent every number in the range that is 0 to 4. Notice we entered 5 as the argument in range, by default the loop starts from 0 and ends at 4. Yes, end at 5 but dont include it. So our output will be 0,1,2,3,4

"""A simple loop that prints 1 to 5 and after printing 5 it prints go using for loop"""
for i in range(1,6):
    print(i)
    if i == 5:
        print('GO')

"""now we are seeing something odd and that is range(). range() is a function that specifies the amount of times an action should be performed. The range function takes a maximum of 3 argument ===> range(start,stop,step). Start: the value you want to start looping from, by default it's 0, Stop: the value you want to end the loop at and finally Step:The number by which the loop varible is being incremented """

# Note: one value entered as an argument in range is taken as stop since by default start is 0, two values entered represents start and stop. And three values entered represents start stop step

"""USING FOR LOOP"""

def get_user_input():
    """This function gets the user input for the multiplication table"""
    user_input = int(input('Enter number'))
    return user_input


def multiplication(value):
    """this function creates a multiplication table with the users input. This multiplication table ends at 12"""
    for number in range(0, 12 + 1):
        answer = number * value
        return f"{number} x {value} = {answer}"

print(multiplication(get_user_input()))

"""Looping through a string"""
name = 'number'
for i in name:
    print(i)
#the output of this program is all the individual characters in number

"""Looping through a list"""
cars = ['benz','toyota','tesla']
for car in cars:
    print(car)
    